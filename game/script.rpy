default rajin = False
default malas = False

label start:

    scene bg intro with fade
    play music audio.intro loop fadein 2.0
    play sound audio.suara_burung fadein 2.0
    "{i}Fajar menyingsing di tanah Kediri.\nKerajaan yang damai dan hijau asri,\ndipimpin oleh Raja Brawijaya, sang penguasa bijak.\n{/i}"
    "{i}Di istananya, hidup seorang putri rupawan bernama Dyah Ayu Pusparani.{/i}"
    
    scene bg kamar_putri with fade
    stop sound fadeout 1.0
    $ renpy.music.set_volume(0.25)

    label pilih:
        default choice_title = "Sekarang, giliran Putri Pusparani ambil keputusan. Pilihannya?"

    menu:
        "Bangun sebelum fajar":
            jump pilih_sebelum
        "Bangun setelah fajar":
            jump pilih_setelah

label pilih_sebelum:
    $ renpy.notify("Pelayan akan mengingat ini...")
    $ rajin = True

    play sound audio.menguap fadein 2.0
    $ renpy.sound.set_volume(1.0)
    show putri normal at kiri
    with dissolve
    PUTRI "Pagi ini sejuk sekali...\nPelayan... pelayan, ke mari sebentar."

    stop sound fadeout 2.0

    play sound audio.buka_pintu volume 1.0
    show pelayan normal at kanan
    with easeinright

    PELAYAN "{i}Sugeng enjing{/i}, Tuan Putri. Adakah perintah yang perlu hamba laksanakan?"
    $ renpy.notify("Sugeng enjing = Selamat pagi")

    $ choice_title = "Putri ingin memulai pagi dengan cara..."

    menu: 
        "Mandi sekarang":
            jump pilih_sekarang
        "Mandi setelah fajar":
            jump pilih_nanti

label pilih_sekarang:
    show putri normal at kiri
    with dissolve
    PUTRI "Aku ingin mandi sekarang. Apakah air hangat telah disiapkan untukku?"
    
    show pelayan normal at kanan
    with dissolve

    PELAYAN "Ada, Tuan Putri. Hamba akan segera menyiapkannya."
    PUTRI "Gelap pagi ini membuat hatiku sedikit gentar. Pelayan, bersediakah kau berjaga selagi aku bersiram?"
    jump lanjut


label pilih_nanti:
    show putri normal at kiri
    with dissolve
    PUTRI "Aku ingin bersiram sekarang. Sudahkah tersedia air hangat untukku?"
    
    show pelayan normal at kanan
    with dissolve
    PELAYAN "Sudah hamba siapkan, Tuan Putri. Gusti bisa bersiram kapan pun berkenan."
    jump lanjut

label pilih_setelah:
    $ renpy.notify("Pelayan akan mengingat ini...")
    $ malas = True
    play sound audio.buka_pintu volume 1.0
    
    show pelayan normal at balik_kiri
    with easeinleft

    PELAYAN "Selamat pagi, Tuan Putri. Apakah Tuan Putri sudah terjaga? Hamba siap mengantarkan Gusti untuk bersiram."
    jump lanjut

label lanjut:
    scene bg tempat_mandi with fade
    play sound audio.air_mengalir loop
    show pelayan normal at balik_kiri
    with easeinleft
    PELAYAN "{i}Ngapunten{/i}, Tuan Putri. Penjaga menyampaikan bahwa Gusti Prabu ingin menemui Tuan Putri setelah selesai bersiram."
    $ renpy.notify("Ngapunten = Permisi")

    hide pelayan normal with dissolve

    label pilih2:
        $ choice_title = "Apa yang akan Tuan Putri lakukan?"

    menu:
        "Putri menunda bertemu":
            jump menunda
        "Putri segera menemui Raja":
            jump bertemu

label menunda:
    stop sound fadeout 2.0
    scene bg kamar_putri with fade

    show putri normal at kiri
    with easeinleft
    PUTRI "Ayahanda ini, ya, selalu memanggilku pagi-pagi. Pelayan, sampaikan pada Ayahanda bahwa aku masih ingin bersantai dulu dan berjalan-jalan di taman."
    
    show pelayan normal at kanan
    with easeinright
    PELAYAN "Namun, Tuan Putri, ada {i}pawartos ingkang wigatos{/i} dari Raja untuk Gusti."
    $ renpy.notify("pawartos ingkang wigatos = kabar penting")
    
    PUTRI "Tidak apa-apa. Setelah berjalan-jalan, aku akan menemui Ayahanda. Bisakah engkau menemaniku berjalan-jalan?"
    
    PELAYAN "Baik, Tuan Putri. Akan saya temani."
    jump lanjut2

label bertemu:
    show putri normal at kiri
    with dissolve
    PUTRI "Ayahanda ingin kutemui di mana, ya?"
    
    show pelayan normal at kanan
    with dissolve
    PELAYAN "Di taman kerajaan, Tuan Putri."

    PUTRI "Ke taman, ya? Hm... sepertinya ini bukan hanya soal bunga yang sedang mekar."
    stop sound fadeout 2.0
    jump lanjut2

label lanjut2:
    scene bg taman_kerajaan with fade
    play sound audio.suara_burung fadein 1.0

    "{i}Bersama pelayannya, Putri melangkah menuju taman tempat Raja menanti.{/i}"

    if rajin:
        show putri normal at balik_kanan
        with dissolve
        show raja senang at balik_kiri
        with easeinleft
        RAJA "Wahai putriku yang rajin, Ayahanda ingin berbincang empat mata denganmu."
        PUTRI "Tentu, Ayahanda. Apa yang ingin Ayahanda sampaikan?"
        jump ngobrol
    elif malas:
        show putri sebal at balik_kanan
        with dissolve
        show raja marah at balik_kiri
        with easeinleft
        RAJA "Ayahanda mendengar dari pelayan bahwa engkau terbangun setelah mentari meninggi, Putriku. Menurutmu, apakah itu mencerminkan sikap seorang putri kerajaan yang patut diteladani?"
        PUTRI "Mohon maaf, Ayahanda. Sebenarnya hamba telah terjaga sejak pagi. Namun udara yang begitu sejuk membuat mata ini kembali terpejam... hanya sejenak."
        jump ngobrol

label ngobrol:  
    show putri normal at balik_kanan
    with dissolve
    show raja normal at balik_kiri
    with dissolve
    RAJA "Putriku, ada hal penting yang perlu Ayahanda sampaikan padamu. Dengarkanlah dengan saksama."
    PUTRI "Ayahanda tampak serius... Apakah yang ingin Ayahanda sampaikan kepada hamba?"

    scene bg diskusi with fade
    RAJA "Ayahanda tahu, ini bukan hal mudah. Namun demi masa depan kerajaan, engkau harus segera menikah."

    play sound audio.menghela_nafas fadein 1.0
    PUTRI "Mengapa tiba-tiba, Ayahanda? Apa yang mendesak hingga keputusan ini harus diambil sekarang?"
    RAJA "Karena Ayahanda percaya, waktumu telah tiba untuk memiliki pendamping yang dapat berjalan bersamamu, bukan hanya sebagai suami, tetapi juga penopang dalam setiap keputusanmu."

    label pilih3:
        $ choice_title = "Langkah apa yang akan diambil oleh Putri Pusparani?"

    menu:
        "Putri tidak ingin menikah":
            jump tidak_ingin
        "Putri ingin menikah tapi belum ada jodoh":
            jump ingin_tapi

label tidak_ingin:
    scene bg taman_kerajaan with fade
    show putri sebal at balik_kanan
    with dissolve
    show raja khawatir at balik_kiri 
    with dissolve

    PUTRI "Tapi saat ini aku belum ingin menikah, Ayah. Aku masih ingin membantu banyak rakyat kita, dan lagipula aku juga belum menemukan calon yang sesuai untukku."
    
    show raja senang at balik_kiri 
    with dissolve
    RAJA "Itu takkan menjadi halangan, Putriku. Bahkan setelah bersuami, engkau tetap dapat mengabdi bagi rakyat. Maka, Ayahanda akan menggelar sebuah sayembara agung, untuk menemukan pendamping yang pantas bagi putri Kerajaan Kediri."
    jump pilih4

label ingin_tapi:
    scene bg taman_kerajaan with fade
    show putri sebal at balik_kanan
    with dissolve
    show raja khawatir at balik_kiri 
    with dissolve

    PUTRI "Ampun Ayahanda... Namun izinkan hamba berterus terang. Saat ini, hamba belum berhasrat untuk menikah. Hamba ingin mengabdikan diri lebih lama bagi rakyat Kediri. Lagipula, hati ini belum menemukan sosok yang sejalan."
    
    show raja senang at balik_kiri 
    with dissolve
    RAJA "Tenanglah, Putriku. Ayah tidak akan menjodohkanmu sembarangan. Ayah sedang mempertimbangkan beberapa sosok yang pantas, yang tak hanya berasal dari darah bangsawan… tapi juga memiliki kecakapan dan hati yang luhur."
    RAJA "Ayah ingin yang terbaik untukmu dan untuk negeri ini."
    PUTRI "Ayahanda. Banyak dari mereka hanya pandai bicara, tapi angkuh dan tak peduli. Aku tak sanggup jika harus hidup bersama orang seperti itu."
    
    show raja marah at balik_kiri
    RAJA "{b}Maka biarlah rakyat dan bangsawan membuktikan diri. Sayembara akan menjadi jalannya. Yang paling pantas, akan menjadi suamimu.{/b}"
    jump pilih4

label pilih4:
    $ choice_title = "Apa yang diinginkan hatimu, Pusparani?"

    menu: 
        "Putri menolak":
            jump menolak
        "Putri menerima":
            jump menerima

label menolak:
    show putri sebal at balik_kanan
    with dissolve
    PUTRI "Ayahanda! Hamba mohon... Jangan paksakan kehendak Ayah. Hamba sudah menyampaikan: Hamba belum siap untuk menikah!"
    
    show raja marah at balik_kiri
    with dissolve
    RAJA "{b}Jangan paksa Ayahanda mengambil keputusan yang tak ingin Ayah ambil. Jika kau tetap menolak, maka pernikahan dengan pangeran dari kerajaan lain akan menjadi jalanmu.{/b}"
    PUTRI "Baiklah, Ayahanda. Jika memang pernikahan harus terjadi... maka izinkan hamba memilih. Hamba ingin pendamping yang rendah hati, bukan yang haus kuasa. Seorang yang mencintai rakyat, bukan hanya takhta."
    RAJA "Maka dengan ini, Ayahanda akan mengadakan sayembara agung. Hanya mereka yang berhati tulus dan mampu membawa kesejahteraan yang pantas menjadi pendampingmu."
    jump lanjut3

label menerima:
    show putri nangis at balik_kanan
    with dissolve
    PUTRI "Baiklah, Ayahanda. Jika itu kehendak Ayah, maka adakanlah sayembara itu. Namun, izinkan hamba berharap bahwa calon yang terpilih benar-benar layak — bagi hamba, dan bagi rakyat kita."
    jump lanjut3

label lanjut3:
    stop audio fadeout 4.0
    scene bg singgasana with fade
    show raja normal at balik_kiri
    with dissolve

    show prajurit normal at kanan
    with dissolve
    play music audio.tegang loop
    $ renpy.music.set_volume(0.3)

    "{i}Atas titah Prabu Brawijaya, pengawal kerajaan telah membawa kabar agung ke seluruh negeri: sayembara untuk meminang Sang Putri telah dimulai.{/i}"
    hide prajurit with easeoutright

    scene bg sayembara with fade
    play sound audio.sorak loop
    "{i}Fajar menyingsing di hari yang telah dijanjikan. Dari segala penjuru negeri, berdatangan para calon: pangeran bersurban megah, pendekar berikat kepala, hingga rakyat jelata dengan tekad membara.{/i}"
    "{i}Semua ingin membuktikan diri mereka layak meminang Sang Putri.{/i}"

    $ renpy.sound.set_volume(0.5)
    show raja senang at balik_kiri 
    with dissolve
    RAJA "Dengarkan semua! Hari ini, Kerajaan Kediri mengadakan sayembara untuk mencari pendamping hidup bagi Putri Dyah Ayu Pusparani. Hanya yang terbaik yang pantas berdiri di sisinya."

    show raja normal at balik_kiri 
    with dissolve
    RAJA "Barang siapa yang mampu merentangkan Busur Kyai Garudayaksa (pusaka para leluhur) dan mengangkat Gong Kyai Sekardelima (lambang kemakmuran negeri ini)."
    RAJA "Dialah yang akan dinobatkan sebagai pemenang sayembara dan berhak mempersunting Putri Dyah Ayu Pusparani."
    
    show raja senang at balik_kiri 
    with dissolve
    RAJA "Kini, tibalah waktunya. Siapa di antara kalian yang hendak menjadi yang pertama menguji diri dalam sayembara ini?"

    # Variabel untuk melacak status keberhasilan
default barang_1_terangkat = False
default barang_2_terangkat = False

# Fungsi untuk mencoba mengangkat barang
init python:
    def coba_angkat_barang(barang):
        if barang == 1:
            return False  # Simulasi kegagalan
        elif barang == 2:
            return False  # Simulasi kegagalan
        return True  # Simulasi keberhasilan

# Screen untuk menampilkan barang sebagai tombol
screen angkat_barang(barang):
    if barang == 1:
        imagebutton:
            idle "busur.png"
            hover "busur.png"
            action [Hide("angkat_barang"), Return(1)]
            xalign 0.5
            yalign 0.5
    elif barang == 2:
        imagebutton:
            idle "gong.png"
            hover "gong.png"
            action [Hide("angkat_barang"), Return(2)]
            xalign 0.5
            yalign 0.5

label mulai_sayembara:
    scene bg sayembara

    # Orang pertama mencoba mengangkat barang pertama
    scene bg sayembara with fade
    play sound audio.sorak loop
    $ renpy.sound.set_volume(0.5)

    show raja normal at kanan
    with dissolve
    show rakyat1 normal at kiri 
    with easeinleft
    ABINAYA "Raja Brawijaya, saya ingin memulai sayembara terlebih dahulu."

    RAJA "Tentu, silakan."
    hide raja normal with dissolve
   
    show rakyat1 normal at center   
    with easeinright
    with hpunch
    play sound audio.hmmm
    call screen angkat_barang(1)
    ABINAYA "{b}HMMRRRGGGGG{/b}, kenapa busur ini berat sekali? {b}HMMRRGGG...{/b}"
    
    $ berhasil = coba_angkat_barang(1)
    if not berhasil:
        ABINAYA "Raja Brawijaya, apa boleh saya mengangkat Gong Kyai Sekardelima terlebih dahulu?"
        $ barang_1_terangkat = False
        $ barang_2_terangkat = False
    
    hide rakyat1 normal with dissolve
    show raja senang at kanan 
    with dissolve
    RAJA "Boleh saja. Jika kamu tidak berhasil melaksanakan keduanya, maka kamu tidak akan menjadi pemenang sayembara."
    hide raja senang with dissolve

    show rakyat1 normal at center
    with vpunch
    with hpunch
    play sound audio.hmmm
    call screen angkat_barang(2)
    ABINAYA "{b}HHHMMMRRGGGGGG...{/b}"

    $ berhasil = coba_angkat_barang(2)
    if not berhasil:
        ABINAYA "Saya menyerah, Raja Brawijaya."
        $ barang_1_terangkat = False
        $ barang_2_terangkat = False


    hide rakyat1 normal with easeoutleft
    show raja senang at kanan
    with dissolve
    RAJA "Baiklah. Selanjutnya!"

    show pangeran normal at balik_kiri
    with easeinleft
    PANGERAN "Raja Brawijaya, izinkan saya mengikuti sayembara ini."

    RAJA "Tentu, Pangeran. Siapa saja bisa ikut sayembara ini."

    hide raja senang with dissolve
    hide pangeran normal with dissolve

    show putri normal at kiri 
    with dissolve
    PUTRI "{i}(Ini kan pangeran yang terkenal sombong dan angkuh. Jangan sampai dia bisa memenangkan sayembara ini.){/i}"

    hide putri normal with dissolve
    show pangeran percaya at balik_kiri 
    with dissolve
    PANGERAN "{i}(Aku kan pangeran paling disegani di negeri ini. Aku pasti bisa! Wahahaha!){/i}"

    show pangeran normal at center
    with easeinright
    with vpunch
    play sound audio.hmmm
    call screen angkat_barang(1)
    PANGERAN "{b}HHHHHMMMMMMMMMM...{/b}"

    $ berhasil = coba_angkat_barang(1)
    if not berhasil:
        PANGERAN "Bagaimana mungkin aku bisa gagal. Aku akan mencoba mengangkat gong nya, yang itu pasti lebih mudah."
        $ barang_1_terangkat = False
        $ barang_2_terangkat = False

    # Orang kedua mencoba mengangkat barang kedua
    show pangeran normal at center
    with hpunch
    play sound audio.hmmm
    call screen angkat_barang(2)
    PANGERAN "{b}HMM HMM HMMMMMM...{/b}"
    
    $ berhasil = coba_angkat_barang(2)
    if not berhasil:
        show pangeran malu at balik_kiri 
        with easeoutleft
        "{i}Pangeran Kadaryan langsung pergi tanpa berkata apa pun.{/i}"
        $ barang_1_terangkat = False
        $ barang_2_terangkat = False

    scene bg colosseum with fade 
    play sound audio.sorak loop
    $ renpy.sound.set_volume(0.5)

    "{i}Hari beranjak siang, dan satu per satu peserta mencoba peruntungan mereka. Namun, tak satu pun berhasil merentangkan busur Kyai Garudayaksa ataupun mengangkat Gong Kyai Sekardelima.{/i}"
    "{i}Sayembara itu pun terasa semakin mustahil untuk ditaklukkan.{/i}"
    "{i}Tiba-tiba, dari arah gerbang utama, muncullah sosok asing. Tubuhnya tegap seperti manusia, namun kepalanya adalah kepala kerbau.{/i}"
    "{i}Dialah Lembu Suro, kini berdiri di hadapan semua orang, menatap lurus ke arah tantangan yang belum terpecahkan.{/i}"

    show raja khawatir at kanan_dikit
    with dissolve
    show putri normal at balik_kanan
    with dissolve
    PUTRI "Siapa dia ayahanda? Kenapa penampilannya sangat mengerikan? Ia memiliki tubuh manusia dengan kepala kerbau"
    RAJA "Hei kamu! perkenalkan siapa dirimu"

    show lembu normal at balik_kiri 
    with easeinleft
    LEMBU "Izin yang mulia Raja Brawijaya, perkenalkan nama saya Lembu suro"

    PUTRI "Ayahanda, aku tidak ingin mendapat calon suami seperti dia, sangat mengerikan, apa kata rakyat kita nantinya"
    
    RAJA "Tenang saja putriku, sampai sekarang ini belum ada yang bisa memenangkan sayembara ini, aku yakin dia juga tidak akan berhasil"

    LEMBU "Apakah saya bisa mengikuti sayembara ini yang mulia?"

    scene bg colosseum with fade 
    
    "{i}Jika raja tidak mengizinkannya mengikuti sayembara, maka raja akan dicap sebagai raja yang buruk karena tidak adil{/i}"
    
    show raja senang at kanan 
    with dissolve
    RAJA "Baiklah silahkan mulai Lembu Suro"

    label game_satu:
    stop music fadeout 2.0
    stop sound fadeout 2.0
    scene bg game with fade
    play music audio.game loop

    "Lembu Suro perlu merentangkan busur untuk menyelesaikan tantangan pertama sayembara."
    "Bantu Lembu Suro memenangkan sayembara dengan menyelesaikan puzzle berikut."
    "Selanjutnya akan diberikan tutorial bagaimana cara bermain puzzle ini!"
    "1. Di layar, kamu akan melihat 8 potongan gambar yang diacak dan satu kotak kosong."
    "2. Klik potongan gambar yang bersebelahan langsung dengan ruang kosong (atas, bawah, kiri, atau kanan)."
    "3. Gambar tersebut akan berpindah ke ruang kosong, dan kamu bisa terus menggeser gambar lainnya."
    "4. Lanjutkan hingga semua potongan kembali tersusun menjadi satu gambar yang lengkap."

    show busur at tengah
    with dissolve
    "Ini gambar lengkap ketika puzzle berhasil disatukan"
    hide busur with dissolve
    "⏳ Waktu Terbatas \nkamu punya 180 detik untuk menyusun gambar dengan benar. Lihat waktu yang tersisa di bagian kiri layar."

    jump mulai_game  # loncat ke label khusus puzzle

label mulai_game:
    window hide
    show screen puzzle_game(folder="puzzle", puzzle=puzzle_1)

    $ renpy.pause(0.1, hard=True)
    $ ui.interact()

    "Berkatmu Lembu Suro dapat merentangkan busur Kyai Garudayaksa!"

    jump setelah_puzzle

    label setelah_puzzle:
        stop music fadeout 2.0
        play sound audio.sorak loop
        $ renpy.sound.set_volume(0.5)
        scene bg sayembara with fade
        "{i}Tak disangka Lembu Suro berhasil merentangkan busur Kyai Garudayaksa.{/i}"

        show putri nangis at kiri
        with dissolve
        PUTRI "Tidak mungkin, bagaimana bisa ia merentangkan busur itu?!?!"
        hide putri nangis with dissolve

        stop music fadeout 2.0 
        stop sound fadeout 2.0
        scene bg sayembara with fade
        play music audio.game loop

        "Selanjutnya Lembu Suro perlu mengangkat gong untuk dapat memenangkan sayembara."
        
        stop music fadeout 2.0
        play sound audio.sorak loop
        $ renpy.sound.set_volume(0.5)
        scene bg kemenangan with fade
        with hpunch
        "{i}Dengan langkah mantap, Lembu Suro mendekati Gong Kyai Sekardelima. Gong yang selama ini dianggap tak tergoyahkan... kini terangkat di tangannya. Semua mata terbelalak. Tak seorang pun menyangka hal itu bisa terjadi.{/i}"

        stop sound fadeout 1.0

        scene bg kecewa with fade
        play sound audio.tangis
        "{i}Tangis sang Putri pecah. Tanpa sepatah kata, ia berlari menuju kamarnya, gaun dan rambutnya tertiup angin. Raja Brawijaya menyusul, langkahnya berat oleh beban perasaan seorang ayah.{/i}"

        scene bg kamar_putri with fade
        show putri nangis at kanan_dikit
        with easeinleft
        PUTRI "Ayahanda! Aku tidak mau dinikahkan dengan manusia berkepala kerbau!"

        show raja khawatir at balik_kiri
        with easeinleft
        RAJA "Maafkan Ayah, Putriku... namun syarat telah ditetapkan, dan ia telah membuktikan dirinya. Ia layak menjadi pendampingmu."
        RAJA "Ayahanda akan membiarkanmu sendiri sejenak."
        hide raja with easeoutleft

    label pilih_menikah:
        $ choice_title = "Apakah Putri menerima lamaran ini?"

    menu:
        "Menerima, dan bersedia menikah":
            jump menikah
        "Tidak menerima": 
            jump tidak_menikah
    
label menikah:
    show putri nangis at kanan_dikit
    with dissolve

    play sound audio.tangis 
    PUTRI "Huuuu... Huuuu... Bagaimana ini? Apakah aku harus menikah dengan seseorang yang berkepala lembu?"
    show pelayan normal at balik_kiri 
    with easeinleft 
    PELAYAN "Ampun, Tuan Putri... bila hamba boleh memberi saran—bagaimana jika Tuan Putri menetapkan satu syarat terakhir? Sebuah ujian bagi Lembu Suro."
    PUTRI "Bagaimana, wahai pelayan? Pikiran ini kusut... yang terbayang hanya nasibku setelah semua ini. Aku tak tahu harus berbuat apa..."
    PELAYAN "Ampun, Tuan Putri. Sungguh hamba punya usul: bagaimanakah kiranya jika paduka memberikan syarat yang sangat berat pada Lembu Suro?"
    PELAYAN "Misalnya, memintanya menggali sumur di puncak Gunung Kelud hanya dalam satu malam. Dan sementara ia sibuk menggali, paduka menyuruh para pengawal menguburnya hidup-hidup..."
    
    show putri ketawa at balik_kanan
    with dissolve
    PUTRI "Ide yang cemerlang, Pelayan. Akan kusampaikan pada Ayahanda—semoga ini menjadi jalan yang membawa terang di tengah gulita hatiku."
    hide putri with easeoutleft
    hide pelayan normal with dissolve
    "{i}Putri menyampaikan permintaan itu dengan hati yang penuh harap kepada Raja Brawijaya. Setelah mendengar dengan seksama, Raja pun mengangguk setuju, memberi restu atas permintaan putrinya.{/i}"
    jump syarat

label tidak_menikah:
    show putri nangis at kanan_dikit
    with dissolve

    play sound audio.tangis
    PUTRI "{i}(menangis){/i} \nAku tidak mau menikah dengan manusia berkepala lembu."
    PUTRI "Pelayan, bagaimana caranya supaya aku tidak harus menikah dengan Lembu Suro?"
    show pelayan normal at balik_kiri 
    with easeinleft
    PELAYAN "Mohon maaf, Tuan Putri, hasil sayembara sudah mutlak dan sah, tidak bisa diubah lagi."
    "{i}(Air mata Putri mengalir deras, suaranya makin keras terdengar menandakan kesedihan yang mendalam.){/i}"

    PELAYAN "Ampun, Tuan Putri. Sungguh hamba punya usul: bagaimanakah kiranya jika paduka memberikan syarat yang sangat berat pada Lembu Suro?"
    PELAYAN "Misalnya, memintanya menggali sumur di puncak Gunung Kelud hanya dalam satu malam. Dan sementara ia sibuk menggali, paduka menyuruh para pengawal menguburnya hidup-hidup..."
    show putri ketawa at balik_kanan
    with dissolve
    PUTRI "Ide yang cemerlang, Pelayan. Akan kusampaikan pada Ayahanda—semoga ini menjadi jalan yang membawa terang di tengah gulita hatiku."
    hide putri with easeoutleft
    hide pelayan normal with dissolve
    "{i}Putri menyampaikan permintaan itu dengan hati yang penuh harap kepada Raja Brawijaya. Setelah mendengar dengan seksama, Raja pun mengangguk setuju, memberi restu atas permintaan putrinya.{/i}" 
    jump syarat 

label syarat:
    stop music fadeout 2.0
    scene bg singgasana with fade
    play music audio.tegang_puol loop
    $ renpy.sound.set_volume(0.3)

    show raja normal at balik_kiri_dikit
    with dissolve
    show putri normal at kiri 
    with dissolve
    show lembu normal at kanan 
    with easeinright
    
    RAJA "Lembu Suro, karena engkau telah memenangkan sayembara, maka engkau berhak menikahi putriku. Namun, putriku ada sesuatu yang ingin ia sampaikan kepadamu."
    
    show lembu senang at kanan 
    with dissolve
    LEMBU "Baik, Yang Mulia, apakah hal yang hendak disampaikan itu?"
    PUTRI "Lembu Suro, sebelum kau menikahiku, aku ingin menyampaikan satu permintaan. Ini akan menjadi syarat terakhir bagimu."
    LEMBU "Apa itu, Tuan Putri?"

    show lembu normal at kanan 
    with dissolve
    PUTRI "Aku ingin kau membangun sumur di puncak Gunung Kelud dalam satu malam. Jika berhasil, kau boleh menikah denganku. Sumur itu akan kita pakai mandi setelah pesta pernikahan nanti."
    
    show lembu senang at kanan 
    with dissolve
    LEMBU "Apakah masih ada permintaan lain dari Tuan Putri?"
    PUTRI "Itu saja, Lembu Suro."

    stop music fadeout 2.0
    play music audio.tegang_puol loop volume 0.5

    scene bg gunung with fade
    show lembu normal at balik_kiri
    with easeinleft
    "{i}Lembu Suro pun mulai melangkah, menembus rimbunnya hutan, menuju puncak Gunung Kelud yang menjulang tinggi.{/i}"

    scene bg hutan with fade
    show lembu normal at balik_kiri
    with easeinleft
    "{i}Sesampainya di puncak Gunung Kelud, Lembu Suro mulai menggali tanah sedikit demi sedikit dengan tanduknya yang kuat.{/i}"

    scene bg puncak_gunung with dissolve
    show lembu normal at balik_kiri
    with easeinleft
    play sound audio.lembu_suro_gali loop

    show lembu marah at balik_kiri
    with dissolve
    "{i}Dengan kesaktiannya, tak butuh waktu lama bagi Lembu Suro untuk menggali tanah hingga cukup dalam.{/i}"

    scene bg gali_puncak_gunung with fade
    show lembu normal at kanan
    with dissolve
    show putri sebal at kiri
    with dissolve
    show prajurit normal at balik_kiri_dikit
    with dissolve

    "{i}Ketika Lembu Suro sudah menggali cukup dalam, Putri datang menghampiri tempat ia sedang menggali.{/i}"

    stop sound fadeout 1.0

    PUTRI "Pengawal, cepat lemparkan batu, tanah, dan garam ke dalam lubang itu! Kubur Lembu Suro hidup-hidup agar ia tak bisa keluar!"
    hide putri sebal with dissolve
    hide prajurit with dissolve
    hide lembu with dissolve

    play sound audio.sapi loop
    
    scene bg gali_puncak_gunung with hpunch
    with vpunch
    "{i}Pengawal pun segera mulai menimbun Lembu Suro dengan batu, tanah, dan garam, memenuhi lubang itu.{/i}"

    scene bg hianat with fade
    "{i}Melihat dirinya telah dikhianati oleh Tuan Putri dan Raja Brawijaya, sebelum ajal menjemput, Lembu Suro mengucapkan sumpah yang menggetarkan hati.{/i}"

    scene bg hianat with hpunch
    with vpunch
    LEMBU "{i}Yoh, Kediri mbesuk bakal pethuk piwalesku sing makaping-kaping, yaiku Kediri bakal dadi kali, Blitar dadi latar, lan Tulungagung dadi kedung{/i}"
    stop sound fadeout 2.0

    scene bg gunung_meletus with vpunch
    play sound audio.meletus fadein 1.0
    with hpunch
    "{i}Mendengar sumpah yang diucapkan oleh Lembu Suro, sampai hari ini, setiap kali Gunung Kelud meletus, dipercaya itu adalah tanda kutukan dari Lembu Suro sebagai balas dendam.{/i}"

    stop sound fadeout 2.0 
    stop music fadeout 2.0

    scene bg kelud vulcano with fade
    play music audio.sedih fadein 2.0

    "{i}Kutukan dari Lembu Suro membawa malapetaka besar bagi Kerajaan Kediri. Sejak saat itu, Gunung Kelud dipercaya menjadi gunung berapi yang aktif dan sering meletus, mengingatkan semua akan amarah sang Lembu.{/i}"
    "{i}Letusan-letusan Gunung Kelud menimbulkan bencana alam dahsyat, merenggut banyak nyawa dan menghancurkan wilayah di sekitarnya.{/i}"

    scene bg kediri banjir with fade
    "{i}Curah hujan yang makin deras membuat sungai-sungai di Kediri meluap, hingga banjir pun jadi peristiwa yang sudah biasa dialami oleh warga kerajaan.{/i}"
    "{i}Banyak yang percaya, semua ini adalah wujud kutukan Lembu Suro yang bersumpah, suatu hari nanti Kediri akan tenggelam dan berubah menjadi lautan.{/i}"
    scene bg blitar latar with fade
    "{i}Blitar bakal berubah jadi daratan luas, laksana halaman terbuka. Blitar jadi simbol tanah datar yang menggambarkan penderitaan dan perubahan besar yang tak terelakkan.{/i}"

    scene bg kedung with fade
    "{i}Tulungagung, di sisi lain, dikutuk menjadi danau luas tak bertepi, sebagai pengingat kelamnya duka yang harus dirasakan oleh para penguasa yang mengkhianati kekuatan Lembu Suro.{/i}"
    
    scene bg pasca malapetaka with fade
    "{i}Pada akhirnya, Kediri berubah menjadi sungai, Blitar menjadi halaman luas, dan Tulungagung menjadi danau. Kisah ini diwariskan turun-temurun selama berabad-abad dan dikenal sebagai Legenda Gunung Kelud.{/i}"
    "{i}Masyarakat setempat meyakini, letusan Gunung Kelud adalah wujud amarah dan kutukan Lembu Suro yang belum terhapus. Hingga kini, kisah itu tetap hidup dan menjadi bagian dari budaya serta kepercayaan masyarakat Jawa Timur.{/i}"
    "{i}Legenda Lembu Suro mengajarkan bahwa ambisi dan keputusan yang diambil tanpa memikirkan perasaan dan kebenaran bisa membawa bencana dan penyesalan besar.{/i}"
    "{i}Kisah ini jadi pengingat buat kita semua tentang pentingnya kejujuran, menghargai sesama, dan hati-hati dalam mengambil keputusan besar.{/i}"

init:
    transform scroll_up:
        yalign 7.0        
        linear 10.0 yalign -5.0  

screen scrolling_credits:
    frame:
        background None
        xalign 0.5
        at scroll_up

        vbox:
            spacing 20
            text "CREDITS" size 50 bold True xalign 0.5
            text "Game Title: Legenda Gunung Kelud: Lembu Suro" size 30 xalign 0.5
            text ""
            text "Game Designer: Muhammad Haidar Allamsyah (5324600001)" xalign 0.5
            text "Programmer: Elsa Hayuningrat (5324600018)" xalign 0.5
            text "Artist: Ehren Gelen Stanislaw (5324600004)" xalign 0.5
            text "Artist: Sulistyawati Adi Putri (5324600008)" xalign 0.5
            text "Artist: Erlangga Rahmansyah (5324600019)" xalign 0.5
            text "Project Manager: Erlangga Rahmansyah (5324600019)" xalign 0.5
            text ""
            text "Special Thanks: Ashafidz Fauzan Dianta, S.ST., M.T." xalign 0.5
            text "Powered by Ren'Py Engine" xalign 0.5
            text ""
            text "Terima kasih telah bermain!" size 35 italic True xalign 0.5


label credits:
    scene black
    show screen scrolling_credits
    with fade

    $ renpy.pause(10.0)  # Durasi kredit scroll

    hide screen scrolling_credits
    return

return
