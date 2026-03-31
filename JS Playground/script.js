// Mengambil elemen layar sekali saja di awal
const layar = document.getElementById('layar-hasil');

function jalankanSapaan() {
    let nama = prompt("Tulis nama Anda:", "Fulan");
    if (nama) {
        layar.innerHTML = `> Hai <strong>${nama}</strong>!<br>> Bagaimana keadaanmu hari ini? Semoga harimu menyenangkan!`;
    } else {
        layar.innerHTML = `> Input dibatalkan oleh pengguna.`;
    }
}

function jalankanIfElse() {
    let izin = confirm("Ingin melihat username Instagram saya?");
    layar.innerHTML = izin ?
        `> Akses diterima!<br>> <strong>Instagram: </strong> parrdhannn` :
        `> Akses ditolak. Terima kasih.`;
}

function jalankanFor() {
    let teks = "> Memulai Iterasi Visual:<br>";
    for (let i = 1; i <= 5; i++) {
        teks += `Proses ke-${i} selesai... <br>`;
    }
    layar.innerHTML = teks;
}

function jalankanMath() {
    let a = 15,
        b = 4;
    layar.innerHTML = `
        > Kalkulasi Matematika (15 & 4):<br>
        > Penjumlahan: <strong>${a + b}</strong><br>
        > Perkalian: <strong>${a * b}</strong><br>
        > Sisa Bagi: <strong>${a % b}</strong>
    `;
}

function jalankanTipeData() {
    layar.innerHTML = `
        > Identifikasi Tipe Data:<br>
        > "Designer" -> <strong>${typeof("Designer")}</strong><br>
        > 2026 -> <strong>${typeof(2026)}</strong><br>
        > window -> <strong>${typeof(window)}</strong>
    `;
}