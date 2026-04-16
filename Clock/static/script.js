const canvas = document.getElementById('clockCanvas');
const ctx = canvas.getContext('2d');
const radius = canvas.width / 2;

// Pindahkan titik 0,0 ke tengah canvas
ctx.translate(radius, radius);

function updateClock() {
    drawFace(ctx, radius);
    drawNumbers(ctx, radius);
    drawTicks(ctx, radius);
    drawTime(ctx, radius);
}

function drawFace(ctx, radius) {
    ctx.clearRect(-radius, -radius, canvas.width, canvas.height);

    // Garis lingkaran dalam
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.95, 0, 2 * Math.PI);
    ctx.strokeStyle = '#3a2818'; // Warna coklat gelap
    ctx.lineWidth = 2;
    ctx.stroke();

    // Garis lingkaran untuk tempat angka
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.75, 0, 2 * Math.PI);
    ctx.lineWidth = 1;
    ctx.stroke();
}

function drawNumbers(ctx, radius) {
    const romanNumerals = ["XII", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI"];
    ctx.font = radius * 0.15 + "px 'Times New Roman', serif";
    ctx.textBaseline = "middle";
    ctx.textAlign = "center";
    ctx.fillStyle = '#1a110a'; // Warna teks hitam kecoklatan

    for (let num = 0; num < 12; num++) {
        let angle = num * Math.PI / 6 - Math.PI / 2;
        let x = Math.cos(angle) * (radius * 0.85);
        let y = Math.sin(angle) * (radius * 0.85);
        ctx.fillText(romanNumerals[num], x, y);
    }
}

function drawTicks(ctx, radius) {
    for (let i = 0; i < 60; i++) {
        let angle = i * Math.PI / 30 - Math.PI / 2;
        let x1 = Math.cos(angle) * (radius * 0.95);
        let y1 = Math.sin(angle) * (radius * 0.95);
        let x2, y2;

        if (i % 5 === 0) {
            x2 = Math.cos(angle) * (radius * 0.88);
            y2 = Math.sin(angle) * (radius * 0.88);
            ctx.lineWidth = 4;
            ctx.strokeStyle = '#1a110a';
        } else {
            x2 = Math.cos(angle) * (radius * 0.92);
            y2 = Math.sin(angle) * (radius * 0.92);
            ctx.lineWidth = 1;
            ctx.strokeStyle = '#3a2818';
        }
        ctx.beginPath();
        ctx.moveTo(x1, y1);
        ctx.lineTo(x2, y2);
        ctx.stroke();
    }
}

function drawTime(ctx, radius) {
    const now = new Date();
    let hour = now.getHours() % 12;
    let minute = now.getMinutes();
    let second = now.getSeconds();

    // Jarum Jam (Hour)
    let hourAngle = (hour + minute / 60) * Math.PI / 6;
    drawHand(ctx, hourAngle, radius * 0.5, radius * 0.06, '#1a110a');

    // Jarum Menit (Minute)
    let minuteAngle = (minute + second / 60) * Math.PI / 30;
    drawHand(ctx, minuteAngle, radius * 0.75, radius * 0.04, '#1a110a');

    // Jarum Detik (Second) - Opsional, di gambar antik tidak ada merah, tapi kita buat tipis
    let secondAngle = second * Math.PI / 30;
    drawHand(ctx, secondAngle, radius * 0.8, radius * 0.01, '#5c4033');

    // Titik tengah (poros jarum)
    ctx.beginPath();
    ctx.arc(0, 0, radius * 0.05, 0, 2 * Math.PI);
    ctx.fillStyle = '#1a110a';
    ctx.fill();
}

function drawHand(ctx, pos, length, width, color) {
    ctx.beginPath();
    ctx.lineWidth = width;
    ctx.lineCap = "round";
    ctx.strokeStyle = color;
    ctx.moveTo(0, 0);
    ctx.rotate(pos);
    ctx.lineTo(0, -length);
    ctx.stroke();
    ctx.rotate(-pos);
}

// Menjalankan fungsi updateClock setiap 1000ms (1 detik) seperti canvas.after(1000) di Python
setInterval(updateClock, 1000);
