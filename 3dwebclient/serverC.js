const socket = new WebSocket('ws://localhost:8001/serverC');

// Connection opened
socket.onopen = () => {
    console.log('✅ Connected to Server B');
};

// Message received from Server B
socket.onmessage = async (event) => {
    try {
        console.log('📨 Message from Server B:', event.data);
        const message = JSON.parse(event.data);

        if (message) {
            console.log('📝 Processing message:', message);
            await flyToCameraPosition(message);

            // Respond back to Server B
            socket.send(JSON.stringify({
                type: "response",
                content: `✅ Flight complete to camera position\n` + JSON.stringify(message, undefined, "\t")
            }));
            console.log('📤 Response sent to Server B');
        } else {
            console.warn('⚠️ Invalid message format:', message);
        }
    } catch (error) {
        console.error('❌ Error parsing message:', error);
    }
};

// Handle connection closure
socket.onclose = (event) => {
    console.log(`🔌 Connection closed (Code: ${event.code}, Reason: ${event.reason})`);
    // Reconnect after delay
    setTimeout(() => {
        console.log('♻️ Attempting to reconnect...');
        location.reload();
    }, 3000);
};

// Handle connection errors
socket.onerror = (error) => {
    console.error('❗ WebSocket Error:', error);
};
