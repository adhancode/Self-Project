from datetime import datetime
import os

file = "dreams.txt"

kamus_tafsir = {
    #MIMPI INDAH
    "bayi": ("Pertanda awal yang baru dan menyenangkan.", "indah"),
    "menikah": ("Kehidupanmu akan lebih bahagia dan harmonis.", "indah"),
    "uang": ("Akan mendapat rezeki tak terduga.", "indah"),
    "terbang": ("Ambisimu besar untuk meraih impian.", "indah"),
    "bunga": ("Mendapat perhatian dan cinta.", "indah"),
    "laut": ("Ketenangan batin dan kedamaian dalam hidup.", "indah"),
    "pelangi": ("Akan datang kebahagiaan setelah masa sulit.", "indah"),
    "makan": ("Menandakan kepuasan dan kebersamaan.", "indah"),
    "matahari": ("Harapan baru dan keberuntungan yang cerah.", "indah"),
    "pelukan": ("Kehangatan dan kasih sayang dari orang terdekat.", "indah"),
    "pohon": ("Pertumbuhan dan kestabilan dalam hidup.", "indah"),
    "burung": ("Kebebasan dan harapan yang tinggi.", "indah"),
    "emas": ("Kekayaan dan keberuntungan yang akan datang.", "indah"),
    "air": ("Ketenangan dan keseimbangan batin.", "indah"),
    "senyum": ("Tanda kebahagiaan dan keberhasilan kecil.", "indah"),
    "mandi": ("Pembersihan diri dari energi negatif.", "indah"),
    "tangga": ("Kemajuan atau perjuangan menuju tujuan.", "indah"),
    "berdoa": ("Ketenangan batin dan harapan baru.", "indah"),
    "mendaki": ("Perjuangan keras akan segera membuahkan hasil.", "indah"),
    "jatuh cinta": ("Kebahagiaan baru dan semangat hidup.", "indah"),
    "menangis": ("Lepasnya beban hati dan kelegaan batin.", "indah"),
    "tertawa": ("Keceriaan dan energi positif di sekitarmu.", "indah"),
    "pesawat": ("Akan ada perjalanan jauh atau peningkatan status.", "indah"),
    "menyapu": ("Membersihkan hal-hal negatif dalam hidup.", "indah"),
    "membaca buku": ("Tanda kebijaksanaan dan ilmu baru.", "indah"),
    "naik sepeda": ("Kemandirian dan keseimbangan hidup.", "indah"),
    "berenang": ("Kemampuan mengendalikan emosi dan situasi.", "indah"),
    "makan nasi": ("Rezeki yang cukup dan ketenangan hati.", "indah"),
    "melihat anak kecil": ("Keceriaan dan kebahagiaan sederhana.", "indah"),
    "melihat ikan": ("Rezeki dan peluang yang datang tiba-tiba.", "indah"),
    "melihat ayam": ("Tanda awal keberhasilan kecil.", "indah"),
    "melihat sapi": ("Kemakmuran dan ketenangan dalam hidup.", "indah"),
    "melihat naga": ("Pertanda kekuatan besar dalam diri sendiri.", "indah"),
    "melihat lebah": ("Kerja kerasmu akan segera membuahkan hasil.", "indah"),
    "melihat kupu-kupu": ("Pertanda transformasi dan keindahan hidup.", "indah"),
    "melihat bintang": ("Impian besar yang bisa tercapai.", "indah"),

    #MIMPI BURUK
    "tenggelam": ("Sedang merasa kewalahan dengan masalah.", "buruk"),
    "hantu": ("Ada ketakutan yang belum terselesaikan.", "buruk"),
    "ular": ("Ada ancaman atau pengkhianatan dari sekitar.", "buruk"),
    "jatuh": ("Kurang percaya diri dan takut gagal.", "buruk"),
    "gelap": ("Kebingungan dan rasa tidak aman.", "buruk"),
    "darah": ("Pertanda kehilangan energi atau semangat.", "buruk"),
    "kematian": ("Akhir dari suatu fase, bukan selalu berarti buruk.", "buruk"),
    "dikejar": ("Ada tekanan atau tanggung jawab yang belum terselesaikan.", "buruk"),
    "banjir": ("Emosi yang meluap dan sulit dikendalikan.", "buruk"),
    "kecelakaan": ("Pertanda kehati-hatian dalam bertindak.", "buruk"),
    "gelas pecah": ("Hubungan atau harapan yang retak.", "buruk"),
    "kebakaran": ("Emosi kuat atau peringatan akan bahaya.", "buruk"),
    "dicuri": ("Kehilangan sesuatu yang berharga, bisa perasaan atau benda.", "buruk"),
    "disakiti": ("Ada luka batin yang belum pulih.", "buruk"),
    "berdarah": ("Pertanda kelelahan fisik atau emosional.", "buruk"),
    "bayangan": ("Bagian diri yang belum kamu terima.", "buruk"),
    "gigi copot": ("Tanda kecemasan atau kehilangan seseorang.", "buruk"),
    "petir": ("Perubahan mendadak yang akan terjadi.", "buruk"),
    "tas hilang": ("Kehilangan tanggung jawab atau rahasia pribadi.", "buruk"),
    "diserang": ("Rasa tidak aman terhadap lingkungan sekitar.", "buruk"),
    "melihat ular besar": ("Ancaman besar yang perlu diwaspadai.", "buruk"),
    "melihat mayat": ("Akhir dari suatu hal yang lama.", "buruk"),
    "melihat buaya": ("Ada orang licik di sekitarmu.", "buruk"),
    "melihat tikus": ("Masalah kecil yang bisa membesar jika diabaikan.", "buruk"),
    "melihat pisau": ("Pertanda konflik atau keputusan sulit.", "buruk"),
    "melihat polisi": ("Rasa bersalah atau takut dihakimi.", "buruk"),
    "melihat bunga layu": ("Hubungan atau harapan yang memudar.", "buruk"),

    #MIMPI BIASA
    "kendaraan": ("Arah hidupmu sedang berubah.", "biasa"),
    "sekolah": ("Memiliki beban tanggung jawab yang meningkat.", "biasa"),
    "teman": ("Butuh dukungan orang-orang terdekat.", "biasa"),
    "rumah": ("Tentang kenyamanan dan kehidupan pribadi.", "biasa"),
    "jalan": ("Sedang mencari arah dan tujuan hidup.", "biasa"),
    "hujan": ("Penyucian diri dan pembaruan emosi.", "biasa"),
    "gunung": ("Tantangan besar yang harus dihadapi.", "biasa"),
    "kucing": ("Simbol intuisi dan kelembutan hati.", "biasa"),
    "anjing": ("Kesetiaan dan perlindungan.", "biasa"),
    "cermin": ("Refleksi diri dan pencarian jati diri.", "biasa"),
    "api": ("Gairah, amarah, atau semangat yang membara.", "biasa"),
    "tidur": ("Butuh istirahat dan menenangkan diri.", "biasa"),
    "berlari": ("Keinginan untuk lari dari masalah atau mencapai tujuan.", "biasa"),
    "senjata": ("Perlindungan diri dan kesiapan menghadapi konflik.", "biasa"),
    "kapal": ("Perjalanan hidup atau perubahan besar.", "biasa"),
    "dimarahi": ("Tanda introspeksi diri agar lebih berhati-hati.", "biasa"),
    "kereta": ("Perjalanan menuju perubahan besar.", "biasa"),
    "motor": ("Ambisi dan arah tujuan hidup yang cepat.", "biasa"),
    "mendengar musik": ("Kedamaian batin dan suasana hati yang cerah.", "biasa"),
    "melihat api": ("Semangat dan kekuatan batin sedang meningkat.", "biasa"),
    "melihat jam": ("Waktu penting semakin dekat, jangan sia-siakan.", "biasa"),
    "melihat jembatan": ("Akan melewati masa transisi hidup.", "biasa"),
    "melihat hujan deras": ("Emosi sedang meluap, tapi akan berakhir damai.", "biasa"),
    "melihat harimau": ("Simbol kekuatan dan tantangan besar.", "biasa"),
    "duduk di kursi": ("Stabilitas dan rasa aman dalam posisi sekarang.", "biasa"),
    "melihat artis": ("Keinginan untuk diperhatikan atau diakui.", "biasa"),
    "bertemu orang mati": ("Pertanda rindu atau pesan dari masa lalu.", "biasa")
}

# Robust parser yang menerima banyak format tanggal
def parse_tanggal_string(tanggal_str):
    if not tanggal_str or not tanggal_str.strip():
        return None

    s = tanggal_str.strip()

    # 1) coba ISO dan beberapa variasi angka
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt)
        except:
            pass

    # 2) coba format bahasa Inggris (Nov, November)
    for fmt in ("%d %b %Y", "%d %B %Y"):
        try:
            return datetime.strptime(s, fmt)
        except:
            pass

    # 3) coba parsing manual untuk bulan bahasa Indonesia (singkatan atau penuh)
    bulan_id = {
        "jan": 1, "januari": 1,
        "feb": 2, "februari": 2,
        "mar": 3, "maret": 3,
        "apr": 4, "april": 4,
        "mei": 5,
        "jun": 6, "juni": 6,
        "jul": 7, "juli": 7,
        "agu": 8, "agustus": 8, "agt": 8,
        "sep": 9, "september": 9,
        "okt": 10, "oktober": 10,
        "nov": 11, "november": 11,
        "des": 12, "desember": 12
    }

    parts = s.replace(",", " ").replace(".", " ").split()
    if len(parts) >= 3:
        # pola umum: DD <bulan> YYYY
        try:
            day = int(parts[0])
            year = int(parts[-1])
            month_token = parts[1].lower()
            month = None
            if month_token in bulan_id:
                month = bulan_id[month_token]
            else:
                # coba ambil 3 huruf awal (mis. 'November' -> 'nov')
                month = bulan_id.get(month_token[:3], None)
            if month and 1 <= day <= 31:
                return datetime(year, month, day)
        except:
            pass

    # gagal parse
    return None

# Fungsi menulis mimpi (simpan tanggal ISO jika kosong)
def tambah_mimpi():
    print("\n=== TULIS MIMPIMU ===")
    nama = input("Nama kamu: ").strip()
    mimpi = input("Ceritakan mimpi kamu: ").strip()
    tanggal = input("Tanggal mimpi: ").strip()

    if tanggal == "":
        tanggal = datetime.now().strftime("%Y-%m-%d")

    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{nama}|{tanggal}|{mimpi}\n")

    print("✨ Mimpi disimpan!\n")

# Baca & hentikan daftar mimpi (urut lama->baru)
def lihat_mimpi(debug=False):
    print("\n=== DAFTAR MIMPI ===")
    if not os.path.exists(file):
        print("Belum ada file mimpi.\n")
        return []

    with open(file, "r", encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f.readlines()]

    if not lines:
        print("Belum ada mimpi yang tercatat.\n")
        return []

    pairs = []
    for line in lines:
        parts = line.split("|", 2)
        if len(parts) < 3:
            # jika format tak standar, letakkan dt=None (di akhir)
            pairs.append((line, None))
            continue
        nama, tanggal_raw, mimpi = parts
        dt = parse_tanggal_string(tanggal_raw)
        pairs.append((line, dt))

    # Sorting: None (gagal parse) akan kita taruh di akhir
    def sort_key(item):
        dt = item[1]
        return dt if dt is not None else datetime.max

    pairs.sort(key=sort_key)

    sorted_lines = [p[0] for p in pairs]

    # tampilkan
    for i, line in enumerate(sorted_lines, start=1):
        parts = line.split("|", 2)
        nama = parts[0] if len(parts) > 0 else ""
        tanggal = parts[1] if len(parts) > 1 else ""
        mimpi = parts[2] if len(parts) > 2 else ""
        print(f"{i}. {nama} | {tanggal} | {mimpi}")
        if debug:
            print(f"   => parsed: {parse_tanggal_string(tanggal)}")
    print()
    return sorted_lines

def ubah_mimpi():
    data = lihat_mimpi()
    if not data:
        return
    try:
        nomor = int(input("Masukkan nomor mimpi yang ingin diubah: ").strip())
    except:
        print("Masukan harus angka.\n"); return
    if not (1 <= nomor <= len(data)):
        print("Nomor tidak valid.\n"); return

    nama = input("Nama baru: ").strip()
    mimpi_baru = input("Isi mimpi baru: ").strip()
    tanggal = input("Tanggal baru (kosong = otomatis): ").strip()
    if tanggal == "":
        tanggal = datetime.now().strftime("%Y-%m-%d")

    data[nomor - 1] = f"{nama}|{tanggal}|{mimpi_baru}"
    # tulis ulang file
    with open(file, "w", encoding="utf-8") as f:
        f.writelines([ln + "\n" for ln in data])
    print("✅ Mimpi diperbarui.\n")

def hapus_mimpi():
    data = lihat_mimpi()
    if not data:
        return
    try:
        nomor = int(input("Masukkan nomor mimpi yang ingin dihapus: ").strip())
    except:
        print("Masukan harus angka.\n"); return
    if not (1 <= nomor <= len(data)):
        print("Nomor tidak valid.\n"); return

    del data[nomor - 1]
    with open(file, "w", encoding="utf-8") as f:
        f.writelines([ln + "\n" for ln in data])
    print("🗑️ Mimpi dihapus.\n")

def tafsir_mimpi():
    data = lihat_mimpi()
    if not data:
        return
    try:
        pilih = int(input("Pilih nomor mimpi untuk ditafsirkan: ").strip())
    except:
        print("Masukan harus angka.\n"); return
    if not (1 <= pilih <= len(data)):
        print("Nomor tidak valid.\n"); return

    parts = data[pilih - 1].split("|", 2)
    nama = parts[0] if len(parts) > 0 else ""
    tanggal = parts[1] if len(parts) > 1 else ""
    mimpi = parts[2] if len(parts) > 2 else ""

    m_lower = mimpi.lower()
    arti = "Tafsir tidak ditemukan."
    kategori = "biasa"
    for kata, detail in kamus_tafsir.items():
        if kata in m_lower:
            arti, kategori = detail
            break

    print("\n=== TAFSIR MIMPI ===")
    print(f"Nama     : {nama}")
    print(f"Tanggal  : {tanggal}")
    print(f"Mimpimu  : {mimpi}")
    print(f"Tafsir   : {arti}")
    print(f"Kategori : {kategori.upper()}\n")

def menu():
    while True:
        print("=== ☁️  MEMORY OF DREAMS 🌙✨ ===")
        print("1. ➕ Tambah Mimpi")
        print("2. 👀 Lihat Semua Mimpi")
        print("3. ✏️  Ubah Mimpi")
        print("4. 🗑️  Hapus Mimpi")
        print("5. 🔮 Tafsir Mimpi")
        print("0. ↩️  Keluar")
        pilih = input("Pilih menu: ").strip()
        if pilih == "1":
            tambah_mimpi()
        elif pilih == "2":
            lihat_mimpi()
        elif pilih == "3":
            ubah_mimpi()
        elif pilih == "4":
            hapus_mimpi()
        elif pilih == "5":
            tafsir_mimpi()
        elif pilih == "0":
            print("Bye 👋")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu()