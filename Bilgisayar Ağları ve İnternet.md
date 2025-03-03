# 🌐 Bilgisayar Ağları ve İnternet: Günümüzün Temel Sistemi

İnternet, insanlığın yarattığı en büyük ve karmaşık sistemlerden biri. Düşünsenize, **milyarlarca** bilgisayar, bağlantı kablosu, sinyal dağıtıcı (anahtar) var. **Milyarlarca** insan da bilgisayarlar, tabletler, akıllı telefonlarla bu ağa bağlı.  Üstelik sadece bilgisayarlar değil, artık televizyonlar, oyun konsolları, evdeki ısı ayarları, güvenlik kameraları, beyaz eşyalar, saatler, gözlükler, arabalar, trafik kontrol sistemleri bile internete bağlanıyor!

İnternet o kadar büyük ve karmaşık ki, "Bu nasıl çalışıyor?" diye sormak çok doğal.  Bu kadar karmaşık bir şeyi anlamak gerçekten mümkün mü? Neyse ki, **evet, mümkün!** 

## İnternet Nedir? Basit Bir Bakış

İnterneti anlamak için iki farklı yol var:

1.  **Temel Parçalarıyla İnternet:** İnterneti oluşturan **donanım ve yazılım** parçalarına bakabiliriz. Yani internetin **"içini"** inceleyebiliriz.
2.  **Hizmetleriyle İnternet:** İnterneti, uygulamalara (mesela web siteleri, uygulamalar) **hizmet veren bir altyapı** olarak düşünebiliriz. Yani internetin **"ne işe yaradığını"** anlayabiliriz.

Şimdi ilk olarak, **"temel parçalarıyla internet"** konusuna odaklanalım.

### İnternetin Temel Taşları: Kablolar, Anahtarlar ve Daha Fazlası

İnternet, dünya üzerindeki **milyarlarca bilgisayarı birbirine bağlayan büyük bir ağ**. Eskiden internete bağlanan cihazlar daha çok masaüstü bilgisayarlar, iş istasyonları ve sunuculardı. Sunucular web sayfaları, e-postalar gibi bilgileri saklar ve gönderirdi.  Ama artık akıllı telefonlar ve tabletler çok yaygınlaştı. Hatta dünya nüfusunun yarısı internete **telefon veya tabletle** giriyor ve bu sayı giderek artıyor.

Televizyonlar, oyun konsolları, ısı ayarları, güvenlik sistemleri, beyaz eşyalar, saatler, gözlükler, arabalar, trafik kontrol sistemleri gibi **alışılmadık pek çok "şey"** de internete bağlanıyor. "Bilgisayar ağı" terimi bile bu kadar farklı cihaz internete bağlanınca biraz eski moda kalıyor.

İnternet dilinde bu cihazların hepsine **"ana bilgisayar" (host)** veya **"uç sistem" (end system)** deniyor.  

Uç sistemler, **bağlantı kabloları (iletişim bağlantıları)** ve **sinyal dağıtıcılar (paket anahtarları)** sayesinde birbirine bağlı. Farklı türde bağlantı kabloları var: **koaksiyel kablo, bakır tel, fiber optik kablo, hatta radyo dalgaları**.  Her bağlantı farklı hızda veri taşıyabilir. Bağlantı hızına **"iletim hızı"** denir ve birimi **bit/saniye (bps)**'dir.

Bir bilgisayar başka bir bilgisayara veri göndermek istediğinde, veri önce **küçük parçalara (segment)** ayrılır. 
Her parçaya **etiket (başlık baytı)** eklenir. Bu etiketlenmiş veri parçalarına **"paket" (packet)** denir. 
Paketler ağ üzerinden gönderilir ve hedefe ulaşınca **tekrar birleştirilerek** orijinal veri elde edilir.

**Sinyal dağıtıcı (paket anahtarı)**, gelen bir paketi alır ve **doğru yöne (giden bağlantıya)** gönderir. 
İki tür sinyal dağıtıcı çok yaygın: **yönlendiriciler (router)** ve **bağlantı katmanı anahtarları (link-layer switch)**. 
İkisi de paketleri hedefe ulaştırmaya çalışır. Bağlantı katmanı anahtarları genellikle **yakın mesafedeki ağlarda** (örneğin ev, ofis), yönlendiriciler ise **internet omurgasında** (ağın merkezinde) kullanılır.  
Bir paketin göndericiden alıcıya giderken geçtiği bağlantılar ve sinyal dağıtıcılar zincirine **"rota" (route) veya "yol" (path)** denir.

**Paket anahtarlamalı ağlar**, aslında **karayolları gibi** çalışır.  
Diyelim ki bir fabrika binlerce kilometre uzaktaki bir depoya mal gönderecek. Mallar paketlenir, kamyonlara yüklenir. 
Her kamyon farklı yollardan depoya gider. Depoya varınca mallar indirilir ve bir araya getirilir. 
İşte internet de böyle çalışır! **Paketler kamyonlara**, **bağlantı kabloları yollara**, **sinyal dağıtıcılar kavşaklara**, **bilgisayarlar ise binalara** benzetilebilir.

Uç sistemler internete **İnternet Servis Sağlayıcıları (ISP)** üzerinden bağlanır. 
Bunlar ev interneti sağlayan şirketler (kablo, telefon şirketleri), iş yeri interneti sağlayan şirketler, üniversite interneti, havaalanları, kafelerdeki WiFi interneti ve cep telefonu interneti gibi farklı türde olabilir. Her ISP aslında kendi içinde bir sinyal dağıtıcı ve bağlantı kabloları ağıdır. 
ISP'ler evlere kablolu (kablo modem, DSL), iş yerlerine hızlı yerel ağ, mobil cihazlara kablosuz gibi farklı internet erişim seçenekleri sunar. 
Ayrıca içerik sağlayıcıların (örneğin web siteleri) sunucularını da internete bağlarlar. 
İnternetin amacı uç sistemleri birbirine bağlamak olduğu için, ISP'lerin de birbirine bağlı olması gerekir. 
Küçük ISP'ler daha büyük ISP'lere, onlar da daha büyük uluslararası ISP'lere bağlıdır. 
En büyük ISP'ler ise hızlı yönlendiriciler ve fiber optik kablolarla birbirine bağlanır. 
Her ISP kendi ağını **bağımsız yönetir**, **IP protokolünü** kullanır ve belirli **adresleme kurallarına** uyar.

İnternet üzerindeki cihazlar (uç sistemler, sinyal dağıtıcılar vb.) bilgiyi göndermek ve almak için **protokoller** kullanır. 
**İletim Kontrol Protokolü (TCP)** ve **İnternet Protokolü (IP)** internetin en temel iki protokolüdür. 
**IP protokolü**, paketlerin formatını (biçimini) belirler. İnternetin temel protokollerine genel olarak **TCP/IP** denir.

Protokollerin internet için çok önemli olduğunu anladık. Bu protokollerin **herkes tarafından aynı şekilde anlaşılması** gerekir ki, farklı insanlar uyumlu sistemler ve ürünler üretebilsin. İşte bu yüzden **standartlar** önemlidir. 
**İnternet standartları**, **İnternet Mühendisliği Görev Gücü (IETF)** tarafından geliştirilir. 
IETF'nin standart belgelerine **Yorum Talepleri (RFC)** denir. 
RFC'ler aslında internetin ilk zamanlarında ortaya çıkan sorunlara çözüm bulmak için **yorum istemek amacıyla** başlamıştır. 
RFC'ler genelde teknik ve detaylı belgelerdir. TCP, IP, HTTP (web için), SMTP (e-posta için) gibi protokolleri tanımlarlar. 
Şu anda yaklaşık 9000+ tane RFC var. **IEEE 802 LAN Standartları Komitesi** gibi başka kuruluşlar da ağ bağlantıları gibi bazı ağ bileşenleri için standartlar belirler. Örneğin, **Ethernet ve WiFi standartlarını** bu komite belirler.

### İnternet Sadece Kablolardan İbaret Değil: Uygulamalara Sunduğu Hizmetler

Yukarıdaki tartışmamızda interneti oluşturan birçok parçayı tanıdık. Ama interneti **tamamen farklı bir açıdan**, yani **uygulamalara hizmet sunan bir altyapı** olarak da tanımlayabiliriz.  Sadece e-posta ve web siteleri gibi klasik uygulamaları düşünmeyin. İnternet uygulamaları artık çok daha çeşitli:

*   **Mobil Uygulamalar:** Akıllı telefon ve tablet uygulamaları (mesajlaşma, haritalar, trafik bilgisi vb.)
*   **Medya Akışı:** Müzik, film, televizyon dizisi yayınları (streaming)
*   **Sosyal Medya:** Online sosyal platformlar
*   **Video Konferans:** Görüntülü toplantı uygulamaları
*   **Çok Oyunculu Oyunlar:** Online, birden fazla kişinin katıldığı oyunlar
*   **Konum Bazlı Öneriler:** Yakındaki mekanları, restoranları öneren sistemler

Bu uygulamaların hepsine **dağıtık uygulamalar (distributed applications)** denir. 
Çünkü birden fazla uç sistemin veri alışverişi yapmasını gerektirirler.  
Önemli bir nokta: **İnternet uygulamaları uç sistemlerde çalışır.** Ağın merkezindeki sinyal dağıtıcılarda (paket anahtarlarında) çalışmazlar. 
Sinyal dağıtıcılar sadece uç sistemler arasında veri alışverişini kolaylaştırır, uygulamanın kendisiyle ilgilenmezler. 
Yani sinyal dağıtıcılar "kargoyu taşır", ama "kargonun ne olduğunu bilmez".

Şimdi "uygulamalara hizmet sunan altyapı" ifadesiyle ne demek istediğimizi biraz daha açalım.  
Diyelim ki aklınıza harika bir internet uygulaması fikri geldi. Belki insanlığa çok faydalı olacak, belki de sizi zengin ve ünlü yapacak bir fikir! 
Bu fikri gerçek bir internet uygulamasına nasıl dönüştürürsünüz?

Uygulamalar uç sistemlerde çalıştığı için, **uç sistemlerde çalışacak programlar yazmanız** gerekecek. 
Programlarınızı Java, C, Python gibi dillerde yazabilirsiniz. Dağıtık bir uygulama geliştirdiğiniz için, farklı uç sistemlerde çalışan programların **birbirleriyle veri göndermesi ve alması** gerekecek. 
İşte burada kritik bir soru ortaya çıkıyor: Bir uç sistemdeki program, başka bir uç sistemdeki programa veri göndermesi için internete nasıl **talimat verir**?

İnternete bağlı uç sistemler, **soket arayüzü (socket interface)** adı verilen bir şey sağlar. 
Soket arayüzü, bir uç sistemdeki programın internet altyapısından başka bir uç sistemdeki **belirli bir programa veri göndermesini nasıl isteyeceğini** belirtir.  Bu arayüz, gönderen programın uyması gereken bir **kurallar bütünüdür**. İnternet, veriyi hedef programa ancak bu kurallara uyulursa ulaştırabilir.

Şimdilik basit bir benzetme yapalım, diyelim ki Ayşe postane aracılığıyla Bob'a mektup göndermek istiyor. 
Ayşe mektubu yazıp pencereden aşağı atamaz, değil mi? Postane, Ayşe'den şunları yapmasını ister:

*   Mektubu bir **zarfa** koymalı.
*   Zarfın ortasına Bob'un **tam adını, adresini ve posta kodunu** yazmalı.
*   Zarfı **kapatmalı**.
*   Zarfın sağ üst köşesine **pul** yapıştırmalı.
*   Son olarak, zarfı resmi bir **posta kutusuna** atmalı.

Yani postanenin kendi "posta hizmeti arayüzü" veya kuralları vardır. 
Ayşe'nin mektubunun Bob'a ulaşması için bu kurallara uyması gerekir. 
İşte internet de benzer şekilde, veri gönderen programın uyması gereken bir **soket arayüzüne** sahiptir. 
Böylece internet, veriyi alacak programa ulaştırabilir.

Postane elbette müşterilerine birden fazla hizmet sunar: hızlı gönderi, teslimat onayı, normal gönderi ve daha pek çok hizmet. 
Benzer şekilde, internet de uygulamalarına **birden fazla hizmet** sunar. 
Bir internet uygulaması geliştirirken, siz de uygulamanız için internetin bu hizmetlerinden birini seçmelisiniz. 

İnterneti şimdiye kadar iki farklı şekilde tanımladık: donanım ve yazılım bileşenleri açısından ve dağıtık uygulamalara hizmet veren bir altyapı açısından. Belki hala internetin ne olduğu konusunda kafanız karışıktır. **Paket anahtarlama ve TCP/IP nedir? Yönlendiriciler nedir? İnternette ne tür bağlantı kabloları var? Dağıtık uygulama nedir? Termostat veya tartı aleti internete nasıl bağlanır?**

### Protokol Nedir? Ağ İletişiminin Kuralları

İnternetin ne olduğunu az çok anladık. Şimdi de bilgisayar ağlarında sıkça duyduğumuz bir başka önemli kelimeye, **protokole** yakından bakalım. 
Protokol nedir? Protokol ne işe yarar?

#### İnsanlarla Protokol: Günlük Hayattan Bir Örnek

Bilgisayar ağı protokollerini anlamak için, önce insan protokollerine bakmak faydalı olabilir. Çünkü biz insanlar da sürekli olarak protokoller uygularız. Örneğin, birinden saati sormak istediğinizde ne yaparsınız? İnsan protokolü (ya da en azından **görgü kuralları**) gereği, önce karşıdaki kişiye **selam vermek** gerekir. "Merhaba"ya tipik cevap yine bir "Merhaba"dır.  Kibar bir "Merhaba" cevabını aldığımızda, saati sormaya devam edebileceğimiz **sinyalini** almış oluruz. İlk "Merhaba"ya farklı bir cevap gelirse ("Rahat bırak beni!", "Ben Türkçe konuşmuyorum!" veya daha kaba bir yanıt gibi), iletişim kurmak istemediğini veya kuramadığını anlarız. Bu durumda, insan protokolü saati sormaktan **vazgeçmeyi** gerektirir. Bazen de soruya hiç cevap alamayız. Bu durumda genellikle o kişiye saati sormaktan vazgeçeriz.

İnsan protokolümüzde, gönderdiğimiz **belirli mesajlar** ve aldığımız **cevap mesajlarına veya diğer olaylara (cevap gelmemesi gibi)** karşılık olarak yaptığımız **belirli eylemler** vardır. Gönderilen ve alınan mesajlar, bu mesajlar gönderildiğinde veya alındığında ya da başka olaylar meydana geldiğinde yapılan eylemler, insan protokolünde **merkezi bir rol oynar**. Eğer insanlar farklı protokoller uygularsa (örneğin, bir kişi görgülü ama diğeri değilse, veya biri zaman kavramını anlıyor ama diğeri anlamıyorsa), protokoller **uyumlu çalışmaz** ve **işe yarar bir sonuç elde edilemez**. 
Aynı durum ağ iletişimi için de geçerlidir: Bir görevi tamamlamak için aynı protokolü çalıştıran **iki (veya daha fazla)** iletişim kuran varlık gerekir.

Başka bir insan örneği düşünelim. Diyelim ki bir üniversite sınıfındasınız (örneğin, bilgisayar ağları dersi!). Öğretmen protokoller hakkında konuşup duruyor ve kafanız karıştı. Öğretmen durur ve "Soru sormak isteyen var mı?" diye sorar (uyuyanlar hariç tüm öğrencilere gönderilen ve alınan bir mesaj). Siz parmağınızı kaldırırsınız (öğretmene **örtülü bir mesaj** gönderirsiniz). Öğretmeniniz size gülümseyerek "Evet..." der (sorunuzu sormanız için sizi **teşvik eden** bir mesaj gönderir - öğretmenler soru sorulmasını sever), ve siz de sorunuzu sorarsınız (yani, öğretmeninize mesajınızı iletirsiniz). Öğretmeniniz sorunuzu duyar (soru mesajınızı alır) ve cevaplar (size bir yanıt gönderir). Bir kez daha görüyoruz ki, mesajların iletilmesi ve alınması, ve bu mesajlar gönderildiğinde ve alındığında yapılan geleneksel eylemler, bu soru-cevap protokolünün merkezinde yer alır.

#### Ağ Protokolleri: Bilgisayarların Ortak Dili

Bir **ağ protokolü**, insan protokolüne benzer. Ancak mesaj alışverişinde bulunan ve eylemde bulunan varlıklar, bir cihazın (örneğin, bilgisayar, akıllı telefon, tablet, yönlendirici veya diğer ağ özellikli cihaz) **donanım veya yazılım bileşenleridir**. 
İnternette iki veya daha fazla uzak varlığın iletişim kurmasını içeren tüm etkinlikler bir protokol tarafından yönetilir. 
Örneğin, fiziksel olarak birbirine bağlı iki bilgisayardaki donanım tarafından uygulanan protokoller, iki ağ arayüz kartı arasındaki "kablo" üzerindeki bit akışını kontrol eder; uç sistemlerdeki tıkanıklık kontrolü protokolleri, gönderici ve alıcı arasında paketlerin iletim hızını kontrol eder; yönlendiricilerdeki protokoller, bir paketin kaynaktan hedefe giden yolunu belirler.

Muhtemelen aşina olduğunuz bir bilgisayar ağı protokolü örneği olarak, bir Web sunucusuna istekte bulunduğunuzda, yani Web tarayıcınıza bir Web sayfasının URL'sini yazdığınızda neler olduğunu düşünün. İlk olarak, bilgisayarınız Web sunucusuna bir **bağlantı isteği mesajı** gönderir ve bir yanıt bekler. 
Web sunucusu sonunda bağlantı isteği mesajınızı alır ve bir **bağlantı yanıtı mesajı** döndürür. Artık Web belgesini istemenin uygun olduğunu anlayan bilgisayarınız, ardından bir **GET mesajı** içinde Web sunucusundan getirmek istediği Web sayfasının adını gönderir. Son olarak, Web sunucusu Web sayfasını (dosyayı) bilgisayarınıza geri gönderir.

Yukarıdaki insan ve ağ iletişimi örnekleri göz önüne alındığında, mesaj alışverişi ve bu mesajlar gönderildiğinde ve alındığında yapılan eylemler, bir protokolün **temel belirleyici unsurlarıdır**:

**Bir protokol, iki veya daha fazla iletişim kuran varlık arasında değiş tokuş edilen mesajların formatını ve sırasını, ayrıca bir mesajın veya başka bir olayın iletimi ve/veya alınması üzerine yapılan eylemleri tanımlar.**

İnternet ve genel olarak bilgisayar ağları, protokolleri **yoğun bir şekilde** kullanır. 
Farklı iletişim görevlerini gerçekleştirmek için farklı protokoller kullanılır.

## Ağın Kenarı(Edge): Bizim Cihazlarımız ve Uygulamalar

Şimdi interneti oluşturan **parçalara biraz daha yakından** bakalım. Bu kısımda ağın **kenarından** başlayacağız. 
Yani en çok tanıdığımız şeylere: **bilgisayarlar, akıllı telefonlar ve günlük kullandığımız diğer cihazlar.** Bir sonraki kısımda ağın kenarından **merkeze** geçip ağlardaki veri yönlendirme işlerine bakacağız.

Hatırlarsanız, bilgisayar ağları dilinde internete bağlı bilgisayarlara ve diğer cihazlara **uç sistemler(end system)** deniyordu. Neden "uç sistemler"? Çünkü bunlar internetin **kenarında** duruyor. İnternetin uç sistemleri neler mi? **Masaüstü bilgisayarlar** (PC'ler, Mac'ler, Linux bilgisayarlar), **sunucular** (web ve e-posta sunucuları), **mobil cihazlar** (dizüstüler, akıllı telefonlar, tabletler) hep uç sistemdir. Hatta artık **alışılmadık "şeyler"** de uç sistem olarak internete bağlanıyor.

Uç sistemlere **ana bilgisayar (host)** da denir. Çünkü bunlar **uygulama programlarını "ağırlıyor" (yani çalıştırıyor)**. 
Mesela web tarayıcısı, web sunucusu, e-posta programı, e-posta sunucusu gibi programlar hep uç sistemlerde çalışır. 

Ana bilgisayarlar bazen ikiye ayrılır: **istemciler (client)** ve **sunucular (server)**. Basitçe söylemek gerekirse, **istemciler** genelde bizim kullandığımız masaüstü bilgisayarlar, dizüstüler, akıllı telefonlar vb. olurken, **sunucular** web sayfalarını saklayan, video yayınlayan, e-posta gönderip alan daha güçlü makinelerdir. Bugün arama sonuçları, e-postalar, web sayfaları, videolar ve mobil uygulama içerikleri aldığımız sunucuların çoğu büyük **veri merkezlerinde (data center)** bulunur. Örneğin, 2020 yılında Google'ın dört kıtada 19 veri merkezi vardı ve buralarda milyonlarca sunucu çalışıyor. 

**VERİ MERKEZLERİ VE BULUT BİLİŞİM**

Google, Microsoft, Amazon, Alibaba gibi internet devleri, her biri **on binlerce, yüz binlerce ana bilgisayarı** barındıran devasa veri merkezleri kurdu. 
Bu veri merkezleri sadece internete bağlı değil, aynı zamanda kendi içlerinde de veri merkezindeki ana bilgisayarları birbirine bağlayan **karmaşık ağlar** var. Veri merkezleri, her gün kullandığımız internet uygulamalarının **motoru** gibidir.

Veri merkezleri genel olarak **üç temel amaca** hizmet eder. Amazon örneği üzerinden gidelim:

1.  **Amazon E-Ticaret Sayfaları:** Kullanıcılara Amazon'un ürün sayfalarını, alışveriş bilgilerini vb. sunar.
2.  **Büyük Veri İşleme:** Amazon'a özel büyük veri işleme görevleri için devasa bir paralel bilgisayar altyapısı görevi görür. Yani aynı anda çok fazla işlem yapabilir.
3.  **Bulut Bilişim (Cloud Computing):** Başka şirketlere bulut hizmetleri sunar. Günümüzde şirketlerin bilgi işlem ihtiyaçlarının çoğunu Amazon gibi bulut sağlayıcılardan karşılaması büyük bir trend. Örneğin, Airbnb gibi birçok internet şirketi kendi veri merkezlerini kurup yönetmek yerine, tüm web hizmetlerini Amazon bulutunda (Amazon Web Services - AWS) çalıştırır.

Veri merkezlerindeki **işçi arılar** ana bilgisayarlardır. Bunlar **içerik sunar** (web sayfaları, videolar), **e-postaları ve belgeleri saklar** ve hep birlikte **büyük hesaplama işlerini** yaparlar. Veri merkezlerindeki ana bilgisayarlara **"blade"** denir ve bunlar pizza kutusuna benzerler. Genelde **standart bilgisayarlardır**, yani özel bir şey değillerdir. İçlerinde işlemci, bellek ve disk depolama bulunur. Bu ana bilgisayarlar **raflara dizilir** ve her rafta genellikle 20-40 tane "blade" bulunur. Raflar da gelişmiş **veri merkezi ağlarıyla** birbirine bağlanır. 

### Erişim Ağları: İnternete Nasıl Bağlanıyoruz?

"Ağın kenarında" ne olduğunu, yani uygulamaları ve uç sistemleri inceledik. 
Şimdi de **erişim ağına** bakalım. Erişim ağı, bir uç sistemi internete bağlayan **ilk adım**. 
Yani bir uç sistemi, herhangi bir uzak uç sisteme giden yoldaki **ilk yönlendiriciye (kenar yönlendiricisi)** fiziksel olarak bağlayan ağdır.

#### Evde İnternet Erişimi: DSL, Kablo, Fiber ve 5G Kablosuz

Evde internet erişim ağlarının bu kadar yaygın kullanımı göz önüne alındığında, erişim ağlarına genel bakışımıza evlerin internete nasıl bağlandığını inceleyerek başlayalım.

Günümüzde en yaygın iki geniş bant ev internet erişim türü **DSL (dijital abone hattı)** ve **kablo internet**tir. 
Evler genellikle DSL internet erişimini, kablolu telefon hizmetini de sağlayan yerel telefon şirketinden (telco) alır. 
Yani DSL kullanıldığında, müşterinin telcosu aynı zamanda ISS'sidir. Her müşterinin DSL modemi, telefon şirketinin yerel merkez ofisinde (CO) bulunan bir DSL erişim çoklayıcısı (DSLAM) ile mevcut telefon hattı üzerinden veri alışverişi yapar. Evin DSL modemi, dijital veriyi alır ve merkez ofise telefon telleri üzerinden iletim için yüksek frekanslı tonlara çevirir; bu tür birçok evden gelen analog sinyaller, DSLAM'da tekrar dijital formata çevrilir.

Ev telefonu hattı, farklı frekanslarda kodlanmış hem veri hem de geleneksel telefon sinyallerini aynı anda taşır:

*   **Yüksek hızlı indirme (download) kanalı:** 50 kHz ila 1 MHz bandında
*   **Orta hızlı yükleme (upload) kanalı:** 4 kHz ila 50 kHz bandında
*   **Sıradan iki yönlü telefon kanalı:** 0 ila 4 kHz bandında

Bu yaklaşım, tek DSL bağlantısının üç ayrı bağlantı varmış gibi görünmesini sağlar, böylece bir telefon görüşmesi ve bir internet bağlantısı aynı anda DSL bağlantısını paylaşabilir. Müşteri tarafında, bir ayırıcı (splitter) eve gelen veri ve telefon sinyallerini ayırır ve veri sinyalini DSL modeme yönlendirir. Telekom tarafında, merkez ofiste, DSLAM veri ve telefon sinyallerini ayırır ve veriyi internete gönderir. Yüzlerce, hatta binlerce hane tek bir DSLAM'a bağlanır.

DSL standartları, 24 Mbps ve 52 Mbps indirme ve 3.5 Mbps ve 16 Mbps yükleme hızları dahil olmak üzere birden fazla iletim hızı tanımlar; 
en yeni standart, 1 Gbps toplu yükleme + indirme hızları sağlar [ITU 2014]. İndirme ve yükleme hızları farklı olduğu için, erişim **asimetrik** olarak adlandırılır. Elde edilen gerçek indirme ve yükleme hızları, DSL sağlayıcısının kademeli hizmet (farklı fiyatlarla sunulan farklı hızlar) sunduğunda konut hızını kasıtlı olarak sınırlayabilmesi nedeniyle yukarıda belirtilen hızlardan daha düşük olabilir. Maksimum hız, evin merkez ofise olan mesafesi, bükümlü çift hattının kalınlığı ve elektriksel parazit derecesi ile de sınırlıdır. Mühendisler, DSL'yi ev ve merkez ofis arasındaki kısa mesafeler için özel olarak tasarlamışlardır; genellikle, konut merkez ofise 5 ila 10 mil içinde bulunmuyorsa, konutun alternatif bir internet erişim şekline başvurması gerekir.

DSL, telekomünikasyon şirketinin mevcut yerel telefon altyapısını kullanırken, kablolu internet erişimi kablolu televizyon şirketinin mevcut kablolu televizyon altyapısını kullanır. Bir konut, kablolu televizyonunu sağlayan aynı şirketten kablolu internet erişimi alır. Fiber optikler kablo merkezini mahalle düzeyindeki kavşaklara bağlar, buradan geleneksel koaksiyel kablo daha sonra bireysel evlere ve apartman dairelerine ulaşmak için kullanılır. Her mahalle kavşağı tipik olarak 500 ila 5.000 evi destekler. Bu sistemde hem fiber hem de koaksiyel kablo kullanıldığı için, genellikle **hibrit fiber koaks (HFC)** olarak adlandırılır.

Kablolu internet erişimi, **kablo modemleri** adı verilen özel modemler gerektirir. 
Bir DSL modeminde olduğu gibi, kablo modemi de tipik olarak harici bir cihazdır ve bir Ethernet portu aracılığıyla ev bilgisayarına bağlanır. 
Kablo merkezinde, kablo modem sonlandırma sistemi (CMTS), DSL ağının DSLAM'ına benzer bir işlev görür; birçok aşağı yönlü evdeki kablo modemlerinden gönderilen analog sinyali tekrar dijital formata çevirir. Kablo modemleri, HFC ağını iki kanala ayırır: bir **aşağı yönlü** ve bir **yukarı yönlü** kanal. 
DSL'de olduğu gibi, erişim tipik olarak **asimetriktir**, aşağı yönlü kanala tipik olarak yukarı yönlü kanaldan daha yüksek bir iletim hızı ayrılır. 
DOCSIS 2.0 ve 3.0 standartları, sırasıyla 40 Mbps ve 1.2 Gbps indirme bit hızlarını ve 30 Mbps ve 100 Mbps yükleme hızlarını tanımlar. 
DSL ağlarında olduğu gibi, daha düşük sözleşmeli veri hızları veya ortam bozulmaları nedeniyle elde edilebilecek maksimum hıza ulaşılamayabilir.

Kablolu internet erişiminin önemli bir özelliği, **paylaşımlı bir yayın ortamı** olmasıdır. 
Özellikle, merkezden gönderilen her paket, her eve giden her bağlantıda aşağı yönde ve bir evden gönderilen her paket yukarı yönlü kanalda merkeze doğru gider. 
Bu nedenle, birden fazla kullanıcı aynı anda aşağı yönlü kanalda bir video dosyası indiriyorsa, her kullanıcının video dosyasını alma hızı, toplam kablolu aşağı yönlü hızdan önemli ölçüde düşük olacaktır. Öte yandan, yalnızca birkaç aktif kullanıcı varsa ve hepsi web'de gezinirken, kullanıcıların her biri aslında tam kablolu aşağı yönlü hızda web sayfaları alabilir, çünkü kullanıcılar nadiren aynı anda bir web sayfası isterler. Yukarı yönlü kanal da paylaşıldığı için, iletimleri koordine etmek ve çarpışmaları önlemek için dağıtılmış çoklu erişim protokolüne ihtiyaç vardır

DSL ve kablolu ağlar şu anda Amerika Birleşik Devletleri'ndeki konut geniş bant erişiminin çoğunluğunu temsil etmesine rağmen, daha yüksek hızlar sağlayan yükselen bir teknoloji **eve fiber (FTTH)**'dir [Fiber Broadband 2020]. Adından da anlaşılacağı gibi, FTTH konsepti basittir; merkez ofisten doğrudan eve bir optik fiber yolu sağlamak. FTTH potansiyel olarak saniyede gigabit aralığında internet erişim hızları sağlayabilir.

Merkez ofisten evlere optik dağıtım için birkaç rakip teknoloji vardır. 
En basit optik dağıtım ağına **doğrudan fiber** denir ve her ev için merkez ofisten bir fiber çıkar. 
Daha yaygın olarak, merkez ofisten çıkan her fiber aslında birçok ev tarafından paylaşılır; fiber evlere nispeten yaklaşana kadar bireysel müşteri özel fiberlere ayrılmaz. Bu ayırmayı gerçekleştiren iki rakip optik dağıtım ağı mimarisi vardır: **aktif optik ağlar (AON'lar)** ve **pasif optik ağlar (PON'lar)**. 
AON esasen anahtarlamalı Ethernet'tir. Burada, Verizon'ın FiOS hizmetinde kullanılan PON'u kısaca tartışıyoruz.

Her evin, özel optik fiber ile bir mahalle ayırıcısına bağlı bir **optik ağ sonlandırıcısı (ONT)** vardır. 
Ayırıcı, bir dizi evi (tipik olarak 100'den az) tek bir paylaşımlı optik fiber üzerinde birleştirir ve bu fiber, 
telekomünikasyon şirketinin merkez ofisindeki bir **optik hat sonlandırıcısına (OLT)** bağlanır. 
Optik ve elektrik sinyalleri arasında dönüşüm sağlayan OLT, bir telekomünikasyon şirketi yönlendiricisi aracılığıyla internete bağlanır. 
Evde, kullanıcılar bir ev yönlendiricisini (tipik olarak bir kablosuz yönlendirici) ONT'ye bağlar ve bu ev yönlendiricisi aracılığıyla internete erişir. 
PON mimarisinde, OLT'den ayırıcıya gönderilen tüm paketler ayırıcıda çoğaltılır (bir kablo merkezine benzer şekilde).

DSL, Kablo ve FTTH'ye ek olarak, **5G sabit kablosuz** da dağıtılmaya başlanıyor. 5G sabit kablosuz sadece yüksek hızlı konut erişimi vaat etmekle kalmıyor, aynı zamanda telekomünikasyon şirketinin merkez ofisinden eve kadar maliyetli ve arıza eğilimli kablolama yapmadan bunu yapacak. 
**Hüzmeleme (beam-forming)** teknolojisini kullanan 5G sabit kablosuz ile, veri bir sağlayıcının baz istasyonundan evdeki bir modeme kablosuz olarak gönderilir. Bir WiFi kablosuz yönlendirici, bir kablo veya DSL modemine bağlı olduğu gibi modeme (muhtemelen birlikte paketlenmiş) bağlanır. 

Burada bahsedilen kavramları daha basitçe özetleyelim.

 * Merkez Ofis(CO): İnternet servis sağlayıcısının (ISS) ana merkezi.

 * Fiber Optik: Verileri ışık sinyalleriyle ileten ince cam liflerinden oluşan kablolar.

 * ONT (Optik Ağ Sonlandırıcısı): Evdeki fiber optik sinyalleri elektrik sinyallerine dönüştüren cihaz.

 * OLT (Optik Hat Sonlandırıcısı): Merkez ofiste bulunan ve fiber optik ağı yöneten cihaz.

 * Ayırıcı (Splitter): Tek bir fiber optik kabloyu birden fazla eve dağıtan cihaz.

 * 5G Sabit Kablosuz: 5G teknolojisi kullanılarak kablosuz olarak internet erişimi sağlayan sistem.

 * Hüzmeleme (Beamforming): 5G'de sinyallerin belirli bir yöne odaklanarak daha güçlü ve istikrarlı bir bağlantı sağlaması.

Fiber Optik İnternet (FTTH) Teknolojileri:

   * Doğrudan Fiber: Her eve ayrı bir fiber optik kablo çekilmesi. Bu, en yüksek bant genişliğini ve en düşük gecikmeyi sağlar, ancak maliyetlidir.

   * PON (Pasif Optik Ağ): Birden fazla evin tek bir fiber optik kabloyu paylaştığı bir mimari. Ayırıcılar kullanılarak sinyaller evlere dağıtılır. Verizon FiOS bu teknolojiyi kullanmaktadır.

#### İş Yerinde ve Evde İnternet: Ethernet ve WiFi

Büyük şirketlerde, üniversitelerde ve artık evlerde de internete bağlanmak için **yerel ağlar (LAN)** kullanılıyor. 
Birçok farklı LAN teknolojisi olsa da, **Ethernet** açık ara en yaygın olanı. 
Özellikle şirketler, üniversiteler ve ev ağlarında Ethernet çok popüler.
Ethernet kullananlar bilgisayarlarını **Ethernet anahtarlayıcıya (switch)** bükümlü çift bakır kablolarla bağlıyor. 
Bu Ethernet anahtarlayıcı veya birbirine bağlı anahtarlayıcılardan oluşan bir ağ, daha sonra internete bağlanıyor. 
Ethernet ile kullanıcılar genelde 100 Mbps'den **10 Gbps'e kadar** hızlara ulaşabilirken, sunucular 1 Gbps'den **10 Gbps'e kadar** hızlara çıkabiliyor.

Ancak günümüzde insanlar internete daha çok **kablosuz olarak** bağlanıyor: dizüstüler, akıllı telefonlar, tabletler... 
Kablosuz yerel ağlarda (WLAN), kablosuz kullanıcılar paketleri **erişim noktasına (access point)** gönderip alıyor. 
Erişim noktası da şirketin ağına (genellikle kablolu Ethernet ile) ve oradan da internete bağlı oluyor. 
Kablosuz LAN kullanıcıları, erişim noktasına **birkaç on metre** yakınında olmalı genelde. 
**WiFi** olarak bilinen ve **IEEE 802.11** standardını kullanan kablosuz LAN'lar artık her yerde karşımıza çıkıyor: üniversiteler, ofisler, kafeler, havaalanları, evler, hatta uçaklarda bile! 802.11 teknolojisi bugünlerde **100 Mbps'den daha yüksek** paylaşım hızları sunabiliyor.

Ethernet ve WiFi erişim ağları ilk başta iş yerleri ve üniversiteler için geliştirilmiş olsa da, artık **ev ağlarında** da çok yaygın. 
Birçok ev, geniş bant internet erişimini (kablo modem veya DSL) ucuz kablosuz LAN teknolojileriyle birleştirerek **güçlü ev ağları** oluşturuyor.

Tipik bir ev ağı örneği. Bu ev ağında:

*   **Kablosuz dizüstü bilgisayar**, **internete bağlı ev aletleri** ve **kablolu bir masaüstü bilgisayar** var.
*   Bir **baz istasyonu (kablosuz erişim noktası)**, kablosuz bilgisayar ve diğer kablosuz cihazlarla iletişim kuruyor.
*   Bir **ev yönlendiricisi (router)**, kablosuz erişim noktasını ve diğer kablolu cihazları internete bağlıyor.

Bu ağ sayesinde ev sakinleri, mutfaktan bahçeye, yatak odasına kadar **her yerden internete** geniş bant hızında erişebiliyor.

#### Geniş Alan Kablosuz Erişim: 3G, 4G (LTE) ve 5G

Akıllı telefonlar (iPhone, Android cihazlar vb.) hareket halindeyken mesajlaşmak, sosyal medyada fotoğraf paylaşmak, mobil ödeme yapmak, film izlemek, müzik dinlemek ve daha birçok şey için kullanılıyor. Bu cihazlar, paketleri cep telefonu şebeke sağlayıcısının işlettiği bir **baz istasyonu** aracılığıyla gönderip almak için cep telefonu teknolojisinde kullanılan **aynı kablosuz altyapıyı** kullanıyor. WiFi'dan farklı olarak, kullanıcının baz istasyonuna sadece **birkaç kilometre (WiFi'da olduğu gibi birkaç on metre değil)** yakınında olması yeterli.

Telekomünikasyon şirketleri, **dördüncü nesil (4G) kablosuz teknolojilere** büyük yatırımlar yaptı. 
4G, gerçek hayatta **60 Mbps'ye kadar indirme hızları** sunabiliyor. Ama daha da hızlı **geniş alan erişim teknolojileri** - **beşinci nesil (5G) geniş alan kablosuz ağları** - şimdiden kullanılmaya başlanıyor. 

### Fiziksel Ortamlar: Veri Kablolar ve Kablosuz Dalgalar

Bu bölümde, internette yaygın olarak kullanılan bu ve diğer **iletim ortamlarına** daha yakından bakacağız.

**Fiziksel ortam** derken ne kastediyoruz? Bir bitin yolculuğunu düşünelim. 
Bir uç sistemden çıkıp, bir sürü bağlantı ve yönlendiriciden geçerek başka bir uç sisteme ulaşıyor. 
Bu minik bit, yol boyunca defalarca aktarılıyor! Gönderen uç sistem biti ilk önce iletiyor, kısa süre sonra ilk yönlendirici biti alıyor, sonra o yönlendirici biti tekrar iletiyor, ikinci yönlendirici alıyor... Bu böyle sürüp gidiyor. Yani bitimiz, kaynaktan hedefe giderken bir dizi **verici-alıcı çiftinden** geçiyor. Her verici-alıcı çiftinde bit, **elektromanyetik dalgalar** veya **ışık sinyalleri** yoluyla bir fiziksel ortam üzerinden gönderiliyor.

Bu **fiziksel ortam** farklı şekil ve türlerde olabilir. 
Yol boyunca her verici-alıcı çifti için aynı türde olması da gerekmiyor. 
Fiziksel ortamlara örnek olarak **bükümlü çift bakır tel**, **koaksiyel kablo**, **çok modlu fiber optik kablo**, **karasal radyo dalgaları** ve **uydu radyo dalgaları** sayılabilir.

Fiziksel ortamlar ikiye ayrılır: **kılavuzlu ortamlar** ve **kılavuzsuz ortamlar**. 
**Kılavuzlu ortamlarda** dalgalar, fiber optik kablo, bükümlü çift bakır tel veya koaksiyel kablo gibi **katı bir ortam** boyunca yönlendirilir. 
**Kılavuzsuz ortamlarda** ise dalgalar atmosferde ve uzay boşluğunda yayılır, örneğin kablosuz LAN veya dijital uydu kanallarında olduğu gibi.

Farklı ortam türlerinin özelliklerine geçmeden önce, **maliyetlerinden** de bahsedelim. 
Fiziksel bağlantının (bakır tel, fiber optik kablo vb.) gerçek maliyeti, diğer ağ maliyetleriyle karşılaştırıldığında genellikle **düşüktür**. 
Asıl maliyet, fiziksel bağlantının **kurulumu** sırasında ortaya çıkan **işçilik maliyetidir**. 
Bu maliyet, malzeme maliyetinden kat kat daha yüksek olabilir. 
Bu nedenle, birçok inşaatçı bir binadaki her odaya bükümlü çift tel, optik fiber ve koaksiyel kablo döşetir. 
Başlangıçta sadece bir ortam kullanılsa bile, yakın gelecekte başka bir ortama ihtiyaç duyulabilir ve gelecekte ek kablo döşemek zorunda kalmamak için baştan hazırlık yapılır.

#### Bükümlü Çift Bakır Kablo: Evlerden Ofislere Her Yerde

En **ucuz** ve **en yaygın** kullanılan kablolu iletim ortamı **bükümlü çift bakır tel**dir. 
Yüz yılı aşkın süredir telefon ağlarında kullanılıyor. 
Hatta telefon ahizesinden yerel telefon santraline kadar olan kablolu bağlantıların %99'undan fazlası bükümlü çift bakır tel kullanır. 
Çoğumuz evlerimizde (veya aile büyüklerimizin evlerinde!) ve iş yerlerimizde bükümlü çift teli görmüşüzdür.

Bükümlü çift tel, her biri yaklaşık 1 mm kalınlığında **iki yalıtımlı bakır telden** oluşur ve düzenli bir spiral şeklinde düzenlenmiştir. 
Teller, yakındaki benzer çiftlerden gelen **elektriksel paraziti azaltmak** için birbirine bükülür. 
Tipik olarak, bir kablodaki bir dizi çift, çiftler koruyucu bir kılıfla sarılarak bir araya getirilir. 
Bir tel çifti, tek bir iletişim bağlantısı oluşturur. **Korumasız bükümlü çift (UTP)**, bir bina içindeki bilgisayar ağları, yani LAN'lar için yaygın olarak kullanılır. Günümüzde bükümlü çift kullanan LAN'lar için veri hızları 10 Mbps ile 10 Gbps arasında değişmektedir. 
Elde edilebilecek veri hızları, telin kalınlığına ve verici ile alıcı arasındaki mesafeye bağlıdır.

1980'lerde fiber optik teknolojisi ortaya çıktığında, birçok kişi nispeten düşük bit hızları nedeniyle bükümlü çift teli küçümsedi. 
Hatta bazıları fiber optik teknolojisinin bükümlü çiftin tamamen yerini alacağını düşündü. 
Ama bükümlü çift tel o kadar kolay pes etmedi. Kategori 6a kablosu gibi modern bükümlü çift tel teknolojisi, yüz metreye kadar mesafeler için 10 Gbps veri hızlarına ulaşabilir. Sonuç olarak, bükümlü çift tel, **yüksek hızlı LAN ağları için baskın çözüm** olarak ortaya çıkmıştır. 
Daha önce de tartıştığımız gibi, bükümlü çift tel konut internet erişimi için de yaygın olarak kullanılmaktadır. 
Çevirmeli modem teknolojisinin bükümlü çift tel üzerinden 56 kbps'ye kadar hızlarda erişim sağladığını gördük. 
Ayrıca DSL (dijital abone hattı) teknolojisinin, konut kullanıcılarının bükümlü çift tel üzerinden (kullanıcılar ISS'nin merkez ofisine yakın yaşadığında) onlarca Mbps hızında internete erişmelerini sağladığını gördük.

#### Koaksiyel Kablo: TV'den İnternete Geniş Kullanım Alanı

**Koaksiyel kablo**, bükümlü çifte benzer şekilde iki bakır iletkenden oluşur. 
Ancak buradaki fark, iki iletkenin **yan yana değil, iç içe** olmasıdır. 
Bu özel yapısı, yalıtımı ve koruması sayesinde koaksiyel kablo **yüksek veri hızlarına** ulaşabilir.

Koaksiyel kablo, **kablo televizyon sistemlerinde** oldukça yaygındır. 
Daha önce gördüğümüz gibi, kablo televizyon sistemleri son zamanlarda kablo modemlerle birleştirilerek ev kullanıcılarına **yüzlerce Mbps hızında internet erişimi** sunmaktadır. Kablolu televizyon ve kablolu internet erişiminde, verici dijital sinyali belirli bir frekans bandına kaydırır ve ortaya çıkan analog sinyal vericiden bir veya daha fazla alıcıya gönderilir.

Koaksiyel kablo, **paylaşımlı bir ortam** olarak da kullanılabilir. 
Yani, birden fazla uç sistem doğrudan kabloya bağlanabilir ve uç sistemlerin her biri diğer uç sistemler tarafından gönderilen her şeyi alır. 
Bu özellik, eski tip ağlarda koaksiyel kablonun yaygın olarak kullanılmasının nedenlerinden biriydi. 
Günümüzde ise daha çok kablolu TV ve internet altyapısında karşımıza çıkıyor.

#### Fiber Optik Kablolar: Işık Hızında Veri İletişimi

**Fiber optik kablo**, ince ve esnek bir ortamdır. İçinden **ışık sinyalleri** göndererek veri iletir. 
Her bir ışık sinyali, bir biti temsil eder. Tek bir fiber optik kablo, **inanılmaz yüksek hızlara** ulaşabilir: saniyede onlarca, hatta yüzlerce gigabit!

**Fiber optik kabloların avantajları:**

*   **Elektromanyetik parazitten etkilenmezler:** Dış etkenlerden kaynaklanan sinyal bozulmaları olmaz.
*   **Sinyal kaybı çok düşüktür:** 100 kilometreye kadar mesafelerde bile sinyal kalitesi bozulmaz.
*   **Dinlenmesi çok zordur:** Veri güvenliği açısından çok avantajlıdır.

Bu özellikler, fiber optik kabloları özellikle **uzun mesafeli iletişimde** (denizaşırı bağlantılar gibi) **en çok tercih edilen kablolu iletim ortamı** yapmıştır. Amerika Birleşik Devletleri ve diğer ülkelerdeki birçok uzun mesafe telefon ağı artık tamamen fiber optik kullanıyor. 
Aynı şekilde, **internet omurgasında** da fiber optik yaygın olarak kullanılıyor.

Ancak **optik cihazların (vericiler, alıcılar, anahtarlayıcılar)** maliyeti hala yüksek olduğu için, fiber optiklerin **kısa mesafelerde** (LAN'lar veya evlere internet erişimi gibi) kullanımı henüz o kadar yaygın değil. **Optik Taşıyıcı (OC)** standardı, bağlantı hızlarını 51.8 Mbps'den 39.8 Gbps'ye kadar değişen aralıklarda tanımlar. Bu hızlar genellikle **OC-n** olarak adlandırılır; burada bağlantı hızı n × 51.8 Mbps'ye eşittir. 
Günümüzde kullanılan standartlar arasında OC-1, OC-3, OC-12, OC-24, OC-48, OC-96, OC-192, OC-768, OC-3072, OC-12288 bulunur. Fiber optik teknolojisi sürekli gelişiyor ve maliyetler düşmeye devam ettikçe, gelecekte daha da yaygınlaşması bekleniyor.

