async function initRealtime() {
  const { client_secret: { value: token }} = await fetch("/session").then(r => r.json());
  const pc = new RTCPeerConnection();
  const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
  pc.addTrack(stream.getTracks()[0]);

  const dc = pc.createDataChannel("oai-events");
  dc.onmessage = e => handleOAI(JSON.parse(e.data));

  const audio = new Audio();
  audio.autoplay = true;
  pc.ontrack = e => (audio.srcObject = e.streams[0]);

  await pc.setLocalDescription(await pc.createOffer());
  const ans = await fetch(`https://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2025-06-03`, {
    method: "POST",
    body: pc.localDescription.sdp,
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/sdp" },
  }).then(r => r.text());
  await pc.setRemoteDescription({ type: "answer", sdp: ans });
}

