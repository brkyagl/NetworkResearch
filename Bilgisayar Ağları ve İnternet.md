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

#### Karasal Radyo Dalgaları

**Radyo dalgaları**, elektromanyetik spektrumda sinyalleri taşır. 
Kablo döşemeye gerek olmaması, duvarlardan geçebilmesi, mobil cihazlara bağlanabilmesi ve uzun mesafelere sinyal iletebilmesi nedeniyle **çekici bir iletişim ortamıdır**.  Radyo kanalının özellikleri, sinyalin yayıldığı **ortama** ve **mesafeye** göre büyük ölçüde değişir. 
Ortam koşulları **sinyal kaybını** ve **gölgelemeyi** (sinyal uzaklaştıkça ve engellerin etrafından dolaştıkça/içinden geçtikçe sinyal gücünün azalması), 
**çoklu yol etkisini** (sinyalin nesnelerden yansımasıyla oluşan girişimler) ve **paraziti** (diğer yayınlar ve elektromanyetik sinyaller nedeniyle) etkiler.

Karasal radyo kanalları genel olarak **üç gruba** ayrılabilir:

*   **Çok kısa mesafe:** Birkaç metre (örneğin, 1-2 metre) içinde çalışanlar.
*   **Yerel alan:** Genellikle on metreden birkaç yüz metreye kadar olan mesafelerde çalışanlar.
*   **Geniş alan:** Onlarca kilometreye kadar ulaşabilenler.

**Kısa mesafe** radyo kanalları kablosuz kulaklık, klavye, tıbbi cihazlar gibi kişisel cihazlarda kullanılır. 
**Yerel alan** radyo kanalları kablosuz LAN (WiFi) teknolojilerinde kullanılır. 
**Geniş alan** radyo kanalları ise hücresel erişim teknolojilerinde (3G, 4G, 5G gibi) kullanılır.

#### Uydu Radyo Kanalları: Uzaydan İnternet

**Uydu iletişim uyduları**, yeryüzündeki **yer istasyonları** adı verilen iki veya daha fazla mikrodalga verici/alıcısını birbirine bağlar. 
Uydu, sinyalleri bir frekans bandında alır, **tekrarlayıcı (repeater)** kullanarak sinyali yeniler (aşağıda açıklanacaktır) ve sinyali başka bir frekansta iletir. İletişimde **iki tür uydu** kullanılır: **yer sabit uydular (geostationary satellites)** ve **alçak yörüngeli uydular (LEO satellites)**.

**Yer sabit uydular**, Dünya üzerinde **aynı noktada sabit** kalır. 
Bu sabitlik, uydunun Dünya yüzeyinden 36.000 kilometre yukarıda bir yörüngeye yerleştirilmesiyle sağlanır. 
Yer istasyonundan uyduya ve tekrar yer istasyonuna olan bu **muazzam mesafe**, 280 milisaniyelik **önemli bir sinyal gecikmesine** neden olur. 
Yine de, **yüzlerce Mbps hızında** çalışabilen uydu bağlantıları, DSL veya kablolu internet erişiminin olmadığı bölgelerde sıklıkla kullanılır.

**Alçak yörüngeli (LEO) uydular** Dünya'ya çok daha yakın yerleştirilir ve Dünya üzerinde **tek bir noktada sabit kalmazlar**. 
Dünya etrafında dönerler (tıpkı Ay gibi) ve hem birbirleriyle hem de yer istasyonlarıyla iletişim kurabilirler. 
Bir bölgeye **kesintisiz kapsama** sağlamak için, yörüngeye birçok uydu yerleştirilmesi gerekir. 
Şu anda geliştirilmekte olan birçok alçak irtifa iletişim sistemi bulunmaktadır. **LEO uydu teknolojisi**, gelecekte internet erişimi için kullanılabilir. Hatta SpaceX'in Starlink projesi gibi bazı LEO uydu internet hizmetleri şimdiden kullanıma sunulmaya başladı bile.

### Ağın Kalbi: Çekirdek Ağ

İnternetin "kenarını" yani uç sistemleri inceledikten sonra, şimdi de ağın **kalbine** doğru yolculuk yapalım: **çekirdek ağ**. 
Çekirdek ağ, internetin uç sistemlerini birbirine bağlayan **paket anahtarları** ve **bağlantıların** oluşturduğu karmaşık bir yapıdır. 


#### Paket Anahtarlama: Veri Nasıl Parçalanıp Taşınıyor?

Bir ağ uygulamasında, uç sistemler birbirleriyle **mesaj** alışverişinde bulunur. 
Mesajlar, uygulama geliştiricisinin istediği her şeyi içerebilir. 
Mesajlar bir **kontrol işlevi** görebilir veya bir e-posta mesajı, bir JPEG resim veya bir MP3 ses dosyası gibi **veri** içerebilir. 
Bir mesajı kaynak uç sistemden hedef uç sisteme göndermek için, kaynak uzun mesajları **paket** olarak bilinen daha küçük veri parçalarına böler. 
Kaynak ve hedef arasında, her paket **iletişim bağlantılarından** ve **paket anahtarlarından** (iki ana türü vardır: yönlendiriciler(routers)
ve bağlantı katmanı anahtarları( link-layer switches)) geçer. Paketler, her iletişim bağlantısı üzerinden bağlantının **tam iletim hızına** eşit bir hızda iletilir. Yani, bir kaynak uç sistemi veya bir paket anahtarı, L bitlik bir paketi R bit/sn iletim hızına sahip bir bağlantı üzerinden gönderiyorsa, paketi iletme süresi **L/R saniye** olur.

L/R ve 2L/R'nin Anlamını Açıklama:

L: Paket boyutu (bit cinsinden). Verinin miktarını temsil ediyor.
R: Bağlantı hızı (bit/saniye). Verinin ne kadar hızlı iletilebileceğini gösteriyor.
L/R: Bir paketi gönderme süresi (saniye). Bir paketin bir bağlantıdan geçmesi için gereken zamanı ifade ediyor.
2L/R: İki bağlantıdan geçme süresi (saniye). Sakla ve ilet yönteminde ilk paketin hedefe ulaşma süresini gösteriyor.

#### Sakla ve İlet Yöntemi: Paketler Nasıl Aktarılıyor?

Çoğu **paket anahtarı (router)**, bağlantılarına gelen paketleri işlerken **sakla ve ilet (store-and-forward)** yöntemini kullanır. 
Bu yöntemde, bir paket anahtarı gelen paketin **tamamını almadan**, paketin ilk bitini **giden bağlantıya** aktarmaya **başlayamaz**.

Bir yönlendiricinin tipik olarak birçok bağlantısı vardır çünkü görevi gelen bir paketi bir giden bağlantıya yönlendirmektir. 
Ancak bir örnekte, yönlendirici sadece bir (giriş) bağlantıdan diğerine (tek giden bağlantıya) paket aktarma görevini yapar. 
Bu örnekte mesela, kaynağın hedefe göndermek üzere her biri **L bit** boyutunda üç paketi olsun. 
Kaynak 1. paketin bir kısmını iletmiş ve 1. paketin başı yönlendiriciye ulaşmıştır bile. 
Yönlendirici sakla ve ilet yöntemini kullandığı için, bu anda yönlendirici aldığı bitleri **hemen iletemez**. 
Önce paketin bitlerini **belleğe kaydetmesi ("saklaması")** gerekir. 
Yönlendirici paketin **tüm bitlerini aldıktan sonra** paketi giden bağlantı üzerinden hedefe doğru **iletmeye ("forward")** başlayabilir.

Sakla ve ilet yöntemini daha iyi anlamak için, kaynağın paketi göndermeye başladığı andan hedef paketin tamamını alana kadar geçen süreyi hesaplayalım. 
(Burada **yayılma gecikmesini** - bitlerin ışık hızına yakın bir hızda tel boyunca hareket etmesi için geçen süreyi - göz ardı ediyoruz.) 
Kaynak, iletime 0 anında başlar; **L/R** saniye sonra, kaynak paketin tamamını iletmiş ve paketin tamamı yönlendiricide alınmış ve saklanmıştır (yayılma gecikmesi olmadığı için). 
**L/R** saniye anında, yönlendirici paketin tamamını yeni aldığı için, paketi giden bağlantı üzerinden hedefe doğru iletmeye başlayabilir; **2L/R** anında, yönlendirici paketin tamamını iletmiş ve paketin tamamı hedef tarafından alınmıştır. 
Yani, **toplam gecikme 2L/R**'dir. Eğer anahtar(switch/router), bitler gelir gelmez (önce paketin tamamını almadan) iletseydi, bitler yönlendiricide bekletilmediği için toplam gecikme L/R olurdu. Ancak, yönlendiricilerin iletmeden önce paketin tamamını alması, saklaması ve işlemesi gerekir.

Şimdi de kaynağın ilk paketi göndermeye başladığı andan hedefin üç paketin tamamını alana kadar geçen süreyi hesaplayalım. 
Daha önce olduğu gibi, **L/R** anında, yönlendirici ilk paketi iletmeye başlar. Ancak **L/R** anında kaynak da ikinci paketi göndermeye başlayacaktır, çünkü ilk paketin tamamını göndermeyi yeni bitirmiştir. Böylece, **2L/R** anında, hedef ilk paketi almış ve yönlendirici ikinci paketi almıştır. Benzer şekilde, **3L/R** anında, hedef ilk iki paketi almış ve yönlendirici üçüncü paketi almıştır. Son olarak, **4L/R** anında hedef üç paketin tamamını almıştır!

Şimdi de kaynaktan hedefe **N bağlantıdan** oluşan bir yol üzerinden (yani, kaynak ve hedef arasında N-1 yönlendirici var) tek bir paket gönderme genel durumunu düşünelim; her bağlantının hızı R olsun. Yukarıdaki mantığı uygulayarak, uçtan uca gecikmenin şu olduğunu görürüz:

```
                        L
d end-to-end =  = N  ____ 
                        R
```

N, kaynak (gönderici) ile hedef (alıcı) arasındaki yol üzerindeki bağlantı sayısını temsil ediyor. 
Metinde "N bağlantıdan oluşan bir yol" denmesinin sebebi bu.

Yönlendiricilerle İlişkisi: Eğer yolda N bağlantı varsa, bu yolda N-1 tane yönlendirici (router) var demektir. Çünkü her yönlendirici iki bağlantıyı birbirine bağlar. Şöyle düşünün: 2 bağlantı için 1 yönlendirici, 3 bağlantı için 2 yönlendirici... N bağlantı için N-1 yönlendirici.

Gecikme Neden Artıyor?  Sakla ve ilet (store-and-forward) yönteminde her yönlendirici, paketin tamamını alıp sonra ilettiği için her bağlantıda L/R kadar bir gecikme oluşuyor.  Yolda ne kadar çok bağlantı (ve dolayısıyla yönlendirici) varsa, gecikme de o kadar katlanıyor. İşte bu yüzden toplam gecikme N * (L/R) oluyor.

Basit Bir Örnek: Kaynak ve hedef arasında sadece 1 yönlendirici olsun. O zaman yol 2 bağlantıdan oluşur (kaynaktan yönlendiriciye, yönlendiriciden hedefe). Yani N=2. Bu durumda gecikme 2 * (L/R) olur, ki bunu zaten önceki örnekte görmüştük.

Şimdi de **P paketinin** N bağlantı üzerinden gönderilmesi durumunda gecikmenin ne olacağını bulmayı deneyebilirsiniz.

P,  gönderilen paket sayısını temsil ediyor. Metinde "Şimdi de P paketinin N bağlantı üzerinden gönderilmesi durumunda gecikmenin ne olacağını bulmayı deneyebilirsiniz." denmesinin sebebi bu.  Yani artık tek paket değil, birden fazla paket gönderiyoruz.

Formül Tek Paket İçin Geçerli: Dikkat ederseniz, d_end-to-end = N * (L/R) formülü tek bir paketin uçtan uca gecikmesini hesaplıyor.  
Yani sadece ilk paketin kaynaktan hedefe ulaşması ne kadar sürer onu buluyoruz.

P Paket Gönderirsek Ne Olur? Eğer P tane paket gönderirsek, ilk paketin gecikmesi hala N * (L/R) olur.  
Çünkü ilk paket diğerlerinden bağımsız olarak aynı yolu takip ediyor ve aynı yönlendiricilerden geçiyor.

Toplam Süre Uzar Ama İlk Paket Gecikmesi Aynı Kalır: P paket gönderdiğimizde toplamda tüm paketlerin hedefe ulaşması daha uzun sürer. Ama ilk paketin gecikmesi değişmez.  Şöyle düşünün: Bir kamyon düşünün ve bu kamyonla koliler taşıyorsunuz. Bir koli taşısanız da, 10 koli taşısanız da ilk kolinin varış süresi aynıdır (eğer yol aynıysa ve trafik yoksa).  Sadece tüm kolilerin teslimatı daha uzun sürer.

Pipelining (Boru Hattı) Kavramı:  Birden fazla paket gönderdiğimizde aslında pipelining (boru hattı) dediğimiz bir durum ortaya çıkar. Kaynak, ilk paketi gönderdikten sonra hemen ikinci paketi, sonra üçüncü paketi... göndermeye başlar. Yönlendiriciler de paketleri art arda işlemeye başlar. Bu sayede ardışık paketlerin hedefe ulaşması arasındaki süre kısalır ve toplam verimlilik artar. Ama ilk paketin gecikmesi temel olarak N * (L/R) olarak kalır.

#### Kuyruk Gecikmeleri ve Paket Kaybı: Ağda Bekleme ve Veri Kaybı

Her **paket anahtarında (router)** birden fazla bağlantı bulunur. 
Bu bağlantıların her biri için, paket anahtarında **çıktı tamponu (output buffer)** veya diğer adıyla **çıktı kuyruğu** adı verilen bir alan vardır. 
Bu alan, yönlendiricinin o bağlantı üzerinden göndermeye hazır olduğu paketleri saklar. output buffer, paket anahtarlamada(packet switching) çok önemli bir rol oynar.

Eğer gelen bir paket bir bağlantı üzerinden iletilmek isterse ancak bağlantı başka bir paketin iletimiyle meşgulse, gelen paket çıktı tamponunda **beklemek zorunda kalır**. 
Yani, sakla ve ilet gecikmelerine ek olarak, paketler çıktı tamponlarında **kuyruk gecikmeleri** de yaşar. Bu gecikmeler **değişkenlik gösterir** ve ağdaki **yoğunluk seviyesine** bağlıdır.

Tampon alanının boyutu **sınırlı** olduğu için, gelen bir paket tamponun iletim için bekleyen diğer paketlerle tamamen dolu olduğunu görebilir. 
Bu durumda **paket kaybı** meydana gelir. Ya gelen paket ya da zaten kuyrukta bekleyen paketlerden biri **düşürülür** (kaybolur).

Diyelim ki A ve B Ana Bilgisayarları, E Ana Bilgisayarına paket gönderiyor. A ve B Ana Bilgisayarları önce paketlerini 100 Mbps Ethernet bağlantıları üzerinden ilk yönlendiriciye gönderir. 
Yönlendirici daha sonra bu paketleri 15 Mbps bağlantısına yönlendirir. Kısa bir süre içinde, yönlendiriciye gelen paketlerin hızı (saniyedeki bit cinsinden) 15 Mbps'yi aşarsa, bağlantının çıktı tamponunda paketler kuyruğa girerken yönlendiricide **yoğunluk** oluşur. Örneğin, A ve B Ana Bilgisayarlarının her biri aynı anda art arda beş paketlik bir veri patlaması gönderirse, bu paketlerin çoğu kuyrukta bir süre beklemek zorunda kalacaktır. Bu durum aslında günlük hayattaki birçok duruma tamamen benzerdir; örneğin, bir banka gişesinde sıra beklemek veya bir gişenin önünde beklemek gibi. 

#### İletim Tabloları ve Yönlendirme Protokolleri

Daha önce, bir yönlendiricinin (router) bağlı olduğu iletişim bağlantılarından birinden gelen bir paketi, bağlı olduğu diğer iletişim bağlantılarından birine ilettiğini söylemiştik. 
Peki, yönlendirici paketi hangi bağlantıya ileteceğini nasıl belirliyor? **Packet forwarding** işlemi aslında farklı bilgisayar ağlarında farklı şekillerde yapılır. 
Burada, bu işlemin internette nasıl yapıldığını kısaca açıklayacağız.

İnternetteki her uç sistemin **IP adresi** adı verilen bir adresi vardır. Bir kaynak uç sistemi bir hedef uç sistemine bir paket göndermek istediğinde, kaynak hedef IP adresini paketin başlığına (header) ekler. Posta adreslerinde olduğu gibi, bu adresin de hiyerarşik bir yapısı vardır. Bir paket ağdaki bir yönlendiriciye ulaştığında, yönlendirici paketin hedef adresinin bir bölümünü inceler ve paketi komşu bir yönlendiriciye iletir. Daha spesifik olarak, her yönlendiricide hedef adresleri (veya hedef adreslerinin bölümlerini) o yönlendiricinin giden bağlantılarına eşleyen bir **iletim tablosu (forwarding table)** bulunur. Bir paket bir yönlendiriciye ulaştığında, yönlendirici adresi inceler ve bu hedef adresini kullanarak uygun giden bağlantıyı bulmak için iletim tablosunu arar. 
Ardından yönlendirici, paketi bu giden bağlantıya yönlendirir.

Uçtan uca yönlendirme süreci, harita kullanmayan ancak yol tarifi sormayı tercih eden bir araba sürücüsüne benzetilebilir. 
Örneğin, diyelim ki Joe, Philadelphia'dan Orlando, Florida'daki 156 Lakeside Drive'a gidiyor. Joe önce mahallesindeki benzin istasyonuna gider ve Orlando, Florida'daki 156 Lakeside Drive'a nasıl gideceğini sorar. Benzin istasyonu görevlisi adresin Florida kısmını alır ve Joe'ya benzin istasyonunun hemen yanındaki girişten I-95 Güney otoyoluna girmesi gerektiğini söyler. Ayrıca Florida'ya girdiğinde orada bir başkasına sorması gerektiğini de belirtir. Joe daha sonra Jacksonville, Florida'ya ulaşana kadar I-95 Güney'i takip eder ve orada başka bir benzin istasyonu görevlisine yol tarifi sorar. 
Görevli adresin Orlando kısmını alır ve Joe'ya I-95'te Daytona Beach'e kadar devam etmesini ve ardından bir başkasına sormasını söyler. 
Daytona Beach'te başka bir benzin istasyonu görevlisi de adresin Orlando kısmını alır ve Joe'ya doğrudan Orlando'ya giden I-4'ü kullanmasını söyler. 
Joe I-4'ü takip eder ve Orlando çıkışından çıkar. Joe başka bir benzin istasyonu görevlisine gider ve bu sefer görevli adresin Lakeside Drive kısmını alır ve Joe'ya Lakeside Drive'a ulaşmak için izlemesi gereken yolu söyler. Joe Lakeside Drive'a ulaştığında, bisikletli bir çocuğa gideceği yeri sorar. Çocuk adresin 156 kısmını alır ve evi işaret eder. Joe sonunda nihai hedefine ulaşır. 
Yukarıdaki benzetmede, benzin istasyonu görevlileri ve bisikletli çocuklar **yönlendiricilere (routers)** benzer.

Az önce bir yönlendiricinin, bir paketin hedef adresini kullanarak bir iletim tablosunu indekslediğini ve uygun giden bağlantıyı belirlediğini öğrendik. 
Ancak bu ifade başka bir soruyu akla getiriyor: İletim tabloları nasıl oluşturulur? Her bir yönlendiricide elle mi yapılandırılırlar yoksa internet daha otomatik bir prosedür mü kullanır? 
Ancak burada merakınızı gidermek için, internetin iletim tablolarını otomatik olarak ayarlamak için kullanılan bir dizi özel **yönlendirme protokolüne (routing protocols)** sahip olduğunu belirtelim. 
Bir yönlendirme protokolü, örneğin, her yönlendiriciden her hedefe en kısa yolu belirleyebilir ve en kısa yol sonuçlarını yönlendiricilerdeki iletim tablolarını yapılandırmak için kullanabilir.

#### Devre Anahtarlama(Circuit Switching)

Veriyi bir ağdaki bağlantılar ve anahtarlar üzerinden taşımanın iki temel yolu vardır: **devre anahtarlama (circuit switching)** ve **paket anahtarlama (packet switching)**. 
Önceki bölümde paket anahtarlamalı ağları inceledik, şimdi de dikkatimizi devre anahtarlamalı ağlara çeviriyoruz.

**Devre anahtarlamalı ağlarda**, uç sistemler arasındaki iletişim için gereken kaynaklar (buffers(tamponlar), bağlantı iletim hızı) iletişim oturumu süresince **ayrılır**. 
**Paket anahtarlamalı ağlarda** ise bu kaynaklar ayrılmaz; bir oturumun mesajları kaynakları ihtiyaç duydukça kullanır ve sonuç olarak bir iletişim bağlantısına erişmek için **beklemek (yani, kuyruğa girmek)** zorunda kalabilirler.

Basit bir benzetme yapacak olursak, biri rezervasyon gerektiren, diğeri ise ne rezervasyon gerektiren ne de kabul eden iki restoran düşünün. 
Rezervasyon gerektiren restorana gitmeden önce telefonla arama zahmetine katlanmamız gerekir. Ancak restorana vardığımızda prensip olarak hemen oturabilir ve yemeğimizi sipariş edebiliriz. 
Rezervasyon gerektirmeyen restoranda ise masa ayırtmamıza gerek yoktur. Ancak restorana vardığımızda oturmadan önce masa beklemek zorunda kalabiliriz.

Geleneksel telefon ağları, **devre anahtarlamalı ağlara** örnektir. Bir kişi telefon şebekesi üzerinden başka birine bilgi (ses veya faks) göndermek istediğinde ne olduğuna bakalım. 
Gönderici bilgiyi göndermeden önce, ağın gönderici ve alıcı arasında bir **bağlantı kurması** gerekir. 
Bu, gönderici ve alıcı arasındaki yoldaki anahtarların bu bağlantı için **bağlantı durumunu** koruduğu gerçek bir bağlantıdır. 
Telefon terminolojisinde bu bağlantıya **devre (circuit)** denir. Ağ devreyi kurduğunda, bağlantı süresince ağın bağlantılarında **sabit bir iletim hızı** (her bağlantının iletim kapasitesinin bir bölümünü temsil eden) da **ayırır**. Belirli bir iletim hızı bu gönderici-alıcı bağlantısı için ayrıldığı için, gönderici veriyi alıcıya **garantili sabit bir hızda** aktarabilir.

Örnek bir ağda, dört devre anahtarı dört bağlantı ile birbirine bağlanmıştır. Bu bağlantıların her birinde dört devre vardır, böylece her bağlantı dört eşzamanlı bağlantıyı destekleyebilir. 
Ana bilgisayarlar (örneğin, PC'ler ve iş istasyonları) doğrudan anahtarlardan birine bağlıdır. 
İki ana bilgisayar iletişim kurmak istediğinde, ağ iki ana bilgisayar arasında **özel bir uçtan uca bağlantı** kurar. 
Bu nedenle, A Ana Bilgisayarının B Ana Bilgisayarı ile iletişim kurabilmesi için, ağın önce iki bağlantının her birinde bir devre ayırması gerekir. 
Örnekte, özel uçtan uca bağlantı, ilk bağlantıdaki ikinci devreyi ve ikinci bağlantıdaki dördüncü devreyi kullanır. 
Her bağlantıda dört devre olduğu için, uçtan uca bağlantı tarafından kullanılan her bağlantı için, bağlantı, bağlantı süresince bağlantının toplam iletim kapasitesinin dörtte birini alır. 
Bu nedenle, örneğin, bitişik anahtarlar arasındaki her bağlantının 1 Mbps'lik bir iletim hızı varsa, her uçtan uca devre anahtarlamalı bağlantı 250 kbps'lik özel bir iletim hızına sahip olur.

Buna karşılık, bir ana bilgisayarın internet gibi bir paket anahtarlamalı ağ üzerinden başka bir ana bilgisayara bir paket göndermek istediğinde ne olduğuna bakalım. 
Devre anahtarlamada olduğu gibi, paket bir dizi iletişim bağlantısı üzerinden iletilir. Ancak devre anahtarlamadan farklı olarak, paket herhangi bir bağlantı kaynağı ayrılmadan ağa gönderilir. 
Bağlantılardan biri aynı anda diğer paketlerin de bağlantı üzerinden iletilmesi gerektiği için yoğunsa, paket iletim bağlantısının gönderen tarafındaki bir tamponda beklemek ve bir gecikme yaşamak zorunda kalacaktır. İnternet, paketleri zamanında teslim etmek için elinden geleni yapar, ancak herhangi bir garanti vermez.

#### Devre Anahtarlamalı Ağlarda Veri Birleştirme (Çoklama)

Devre anahtarlamalı ağlarda bir bağlantıdaki devre, temelde iki yöntemle oluşturulur: **frekans bölmeli çoklama (Frequency-Division Multiplexing - FDM)** veya **zaman bölmeli çoklama (Time-Division Multiplexing - TDM)**.

**Frekans Bölmeli Çoklama (FDM):** Bu yöntemde, bir bağlantının frekans aralığı, o bağlantı üzerinden kurulan farklı iletişimler arasında paylaştırılır. 
Yani, bağlantı süresince her bir iletişim için **ayrı bir frekans bandı** ayrılır. Telefon ağlarında bu frekans bandı genellikle 4 kHz genişliğindedir (4000 Hertz veya saniyede 4000 döngü). 
Bu bandın genişliğine de tahmin edebileceğiniz gibi **bant genişliği (bandwidth)** denir. FM radyo istasyonları da 88 MHz ile 108 MHz arasındaki frekans aralığını paylaşmak için FDM'yi kullanır ve her istasyona belirli bir frekans bandı tahsis edilir.

**Zaman Bölmeli Çoklama (TDM):** Bu yöntemde ise zaman, sabit süreli **çerçevelere (frame)** bölünür ve her çerçeve sabit sayıda **zaman dilimine (time slot)** ayrılır. 
Ağ bir bağlantı üzerinden bir iletişim kurduğunda, ağ her çerçevedeki bir zaman dilimini bu iletişime ayırır. 
Bu zaman dilimleri sadece o iletişimin kullanımı içindir ve her çerçevede bir zaman dilimi, o bağlantının verilerini iletmek için kullanılabilir.

Örneğin, dört adede kadar devreyi destekleyen belirli bir ağ bağlantısı için FDM ve TDM olsun. FDM için, frekans alanı her biri 4 kHz bant genişliğine sahip dört banda ayrılmıştır. 
TDM için ise zaman alanı çerçevelere bölünmüştür ve her çerçevede dört zaman dilimi vardır; her devre, dönen TDM çerçevelerinde aynı ayrılmış zaman dilimine atanır. 
TDM için, bir devrenin iletim hızı, çerçeve hızı ile bir zaman dilimindeki bit sayısının çarpımına eşittir. Örneğin, bağlantı saniyede 8000 frames iletiyorsa ve her zaman dilimi 8 bitten oluşuyorsa, her devrenin iletim hızı 64 kbps'dir.

Paket anahtarlama savunucuları her zaman devre anahtarlamanın **kaynak israfı** olduğunu savunmuşlardır çünkü ayrılan devreler sessiz dönemlerde boştur. 
Örneğin, bir telefon görüşmesinde bir kişi konuşmayı bıraktığında, bağlantının yolu üzerindeki bağlantılardaki boş ağ kaynakları (frekans bantları veya zaman dilimleri) diğer devam eden bağlantılar tarafından kullanılamaz. Bu kaynakların nasıl yetersiz kullanılabileceğine başka bir örnek olarak, bir radyologun bir devre anahtarlamalı ağı kullanarak bir dizi röntgene uzaktan eriştiğini düşünün. 
Radyolog bir bağlantı kurar, bir görüntü ister, görüntüyü inceler ve ardından yeni bir görüntü ister. Ağ kaynakları bağlantıya tahsis edilir ancak radyologun inceleme süreleri boyunca kullanılmaz (yani, boşa harcanır). Paket anahtarlama savunucuları ayrıca uçtan uca devreler kurmanın ve uçtan uca iletim kapasitesi ayırmanın karmaşık olduğunu ve uçtan uca yoldaki anahtarların çalışmasını koordine etmek için karmaşık sinyal yazılımı gerektirdiğini de belirtmekten hoşlanırlar.

Devre anahtarlama tartışmamızı bitirmeden önce, konuya daha fazla ışık tutacak sayısal bir örnek çözelim. 
Bir devre anahtarlamalı ağ üzerinden A Ana Bilgisayarından B Ana Bilgisayarına 640.000 bitlik bir dosyanın ne kadar sürede gönderileceğini düşünelim. 
Ağdaki tüm bağlantıların 24 zaman dilimli TDM kullandığını ve 1.536 Mbps bit hızına sahip olduğunu varsayalım. 
Ayrıca, A Ana Bilgisayarının dosyayı iletmeye başlamadan önce uçtan uca bir devre kurmasının 500 milisaniye sürdüğünü varsayalım. 
Dosyayı göndermek ne kadar sürer? Her devrenin iletim hızı (1.536 Mbps) / 24 = 64 kbps'dir, bu nedenle dosyayı iletmek (640.000 bit) / (64 kbps) = 10 saniye sürer. 
Bu 10 saniyeye devre kurma süresini de eklersek, dosyayı göndermek toplam 10.5 saniye sürer. İletim süresinin bağlantı sayısından bağımsız olduğuna dikkat edin: Uçtan uca devre bir bağlantıdan veya yüz bağlantıdan geçse bile iletim süresi 10 saniye olurdu.

#### Paket Anahtarlama mı, Devre Anahtarlama mı?

Devre anahtarlama ve paket anahtarlamayı açıkladıktan sonra, şimdi bu iki yöntemi karşılaştıralım.

Paket anahtarlama eleştirmenleri, bu yöntemin değişken ve öngörülemeyen uçtan uca gecikmeleri (esas olarak değişken ve öngörülemeyen kuyruk gecikmelerinden kaynaklanır) nedeniyle **gerçek zamanlı hizmetler** (örneğin, telefon görüşmeleri ve video konferans görüşmeleri) için uygun olmadığını sık sık savunmuşlardır. 
Ancak paket anahtarlama savunucuları ise şu argümanları öne sürerler: (1) devre anahtarlamaya göre **iletim kapasitesini daha iyi paylaşır** ve (2) devre anahtarlamaya göre **uygulaması daha basit, daha verimli ve daha az maliyetlidir**. Genel olarak konuşmak gerekirse, restoran rezervasyonlarıyla uğraşmaktan hoşlanmayanlar devre anahtarlamaya kıyasla paket anahtarlamayı tercih ederler.

Peki, paket anahtarlama neden daha verimli? Basit bir örneğe bakalım. Diyelim ki kullanıcılar 1 Mbps'lik bir bağlantıyı paylaşıyorlar. 
Ayrıca, her kullanıcının aktif olduğu dönemlerde sabit bir 100 kbps hızında veri ürettiğini ve aktif olmadığı dönemlerde ise hiç veri üretmediğini varsayalım. 
Dahası, bir kullanıcının zamanın sadece %10'unda aktif olduğunu (ve geri kalan %90'ında kahvesini yudumladığını) varsayalım. 
Devre anahtarlamada, her kullanıcı için her zaman 100 kbps **ayrılması** gerekir. Örneğin, devre anahtarlamalı TDM ile, bir saniyelik bir çerçeve her biri 100 ms'lik 10 zaman dilimine bölünürse, her kullanıcıya çerçeve başına bir zaman dilimi tahsis edilir.

Bu nedenle, devre anahtarlamalı bağlantı aynı anda yalnızca 10 (= 1 Mbps / 100 kbps) kullanıcıyı destekleyebilir. 
Paket anahtarlamada ise belirli bir kullanıcının aktif olma olasılığı 0.1'dir (yani %10). 35 kullanıcı varsa, aynı anda 11 veya daha fazla aktif kullanıcının olma olasılığı yaklaşık olarak 0.0004'tür.
Aynı anda 10 veya daha az aktif kullanıcı olduğunda (ki bu %0.9996 olasılıkla gerçekleşir), verinin toplam geliş hızı bağlantının çıkış hızına eşit veya daha düşüktür (1 Mbps). 
Bu nedenle, 10 veya daha az aktif kullanıcı olduğunda, kullanıcıların paketleri bağlantıdan esasen devre anahtarlamada olduğu gibi **gecikmesiz** akar. 
Aynı anda 10'dan fazla aktif kullanıcı olduğunda ise paketlerin toplam geliş hızı bağlantının çıkış kapasitesini aşar ve çıktı kuyruğu büyümeye başlar. (Toplam giriş hızı 1 Mbps'nin altına düşene kadar büyümeye devam eder, bu noktada kuyruk küçülmeye başlar.) Bu örnekte aynı anda 10'dan fazla aktif kullanıcının olma olasılığı çok düşük olduğundan, paket anahtarlama esasen devre anahtarlama ile aynı performansı sağlar, ancak bunu üç katından fazla kullanıcıya izin vererek yapar.

Şimdi de ikinci basit bir örneğe bakalım. Diyelim ki 10 kullanıcı var ve bir kullanıcı aniden bin adet 1000 bitlik paket üretiyor, diğer kullanıcılar ise sessiz kalıyor ve paket üretmiyorlar. 
Çerçeve başına 10 zaman dilimi olan ve her zaman dilimi 1000 bitten oluşan TDM devre anahtarlamasında, aktif kullanıcı veri iletmek için çerçeve başına yalnızca bir zaman dilimini kullanabilirken, her çerçevedeki kalan dokuz zaman dilimi boş kalır. Aktif kullanıcının bir milyon bitlik verisinin tamamının iletilmesi 10 saniye sürer. Paket anahtarlama durumunda ise aktif kullanıcı, diğer kullanıcıların paketleriyle **çoklanması (multiplexed)** gereken başka kullanıcı olmadığı için paketlerini 1 Mbps'lik tam bağlantı hızında sürekli olarak gönderebilir. Bu durumda, aktif kullanıcının tüm verileri 1 saniye içinde iletilir.

Yukarıdaki örnekler, paket anahtarlamanın performansının devre anahtarlamanın performansından üstün olabileceği iki yolu göstermektedir. 
Ayrıca, bir bağlantının iletim hızının birden çok veri akışı arasında paylaşılmasının bu iki biçimi arasındaki temel farkı da vurgulamaktadır. 
Devre anahtarlama, talebe bakılmaksızın iletim bağlantısının kullanımını önceden tahsis eder ve tahsis edilen ancak gerekmeyen bağlantı süresi kullanılmadan kalır. 
Paket anahtarlama ise bağlantı kullanımını talep üzerine tahsis eder. Bağlantı iletim kapasitesi, yalnızca bağlantı üzerinden iletilmesi gereken paketleri olan kullanıcılar arasında paket paket bazında paylaşılır.

Paket anahtarlama ve devre anahtarlama günümüz telekomünikasyon ağlarında yaygın olsa da, eğilim kesinlikle paket anahtarlamaya doğru olmuştur. 
Günümüzün devre anahtarlamalı telefon ağlarının çoğu bile yavaş yavaş paket anahtarlamaya geçmektedir. Özellikle telefon ağları, bir telefon görüşmesinin pahalı denizaşırı kısmı için genellikle paket anahtarlamayı kullanır.

#### Ağların Ağı

Daha önce uç sistemlerin (PC'ler, akıllı telefonlar, Web sunucuları, e-posta sunucuları vb.) bir **erişim İSS'si (access ISP)** aracılığıyla internete bağlandığını görmüştük. Erişim İSS'si, DSL, kablo, FTTH, Wi-Fi ve hücresel gibi çeşitli erişim teknolojilerini kullanarak kablolu veya kablosuz bağlantı sağlayabilir. Erişim İSS'sinin bir telekom şirketi veya kablo şirketi olmak zorunda olmadığını unutmayın; bunun yerine, örneğin bir üniversite (öğrencilere, personele ve öğretim üyelerine internet erişimi sağlayan) veya bir şirket (çalışanlarına erişim sağlayan) olabilir. Ancak son kullanıcıları ve içerik sağlayıcıları bir erişim İSS'sine bağlamak, interneti oluşturan milyarlarca uç sistemi birbirine bağlama bulmacasının yalnızca küçük bir parçasıdır. Bu bulmacayı tamamlamak için, erişim İSS'lerinin kendilerinin de **birbirine bağlanması** gerekir. İşte bu, **ağların ağı** oluşturularak yapılır—bu ifadeyi anlamak, interneti anlamanın anahtarıdır.

Yıllar içinde, interneti oluşturan ağların ağı çok karmaşık bir yapıya evrilmiştir. Bu evrimin çoğu performans kaygılarından ziyade ekonomi ve ulusal politikalar tarafından yönlendirilmiştir. Günümüzün internet ağ yapısını anlamak için, her yeni yapının bugünkü karmaşık internete daha iyi bir yaklaşım olduğu bir dizi ağ yapısını adım adım oluşturalım. Temel amacın, tüm uç sistemlerin birbirine paket gönderebilmesi için erişim İSS'lerini birbirine bağlamak olduğunu hatırlayalım. Naif bir yaklaşım, her erişim İSS'sinin diğer her erişim İSS'sine doğrudan bağlanması olurdu. Ancak böyle bir örgü tasarım, her erişim İSS'sinin dünya çapındaki yüz binlerce diğer erişim İSS'sine ayrı bir iletişim bağlantısına sahip olmasını gerektireceğinden, erişim İSS'leri için çok maliyetli olurdu.

İlk ağ yapımız, **Ağ Yapısı 1**, tüm erişim İSS'lerini tek bir **küresel transit İSS (global transit ISP)** ile birbirine bağlar. Bizim (hayali) küresel transit İSS'miz, yalnızca dünyayı kapsamakla kalmayıp aynı zamanda yüz binlerce erişim İSS'sinin her birinin yakınında en az bir yönlendiriciye sahip olan bir yönlendirici ve iletişim bağlantıları ağıdır. Elbette, küresel İSS'nin bu kadar kapsamlı bir ağ kurması çok maliyetli olacaktır. Kârlı olmak için, doğal olarak her bir erişim İSS'sinden bağlantı için ücret alacak ve fiyatlandırma, bir erişim İSS'sinin küresel İSS ile alışveriş yaptığı trafik miktarına yansıtacaktır (ancak doğrudan orantılı olmak zorunda değildir). Erişim İSS'si küresel transit İSS'ye ödeme yaptığı için, erişim İSS'sine **müşteri (customer)** ve küresel transit İSS'ye **sağlayıcı (provider)** denir.

Şimdi, eğer bir şirket kârlı bir küresel transit İSS kurar ve işletirse, diğer şirketlerin de kendi küresel transit İSS'lerini kurması ve orijinal küresel transit İSS ile rekabet etmesi doğaldır. Bu, yüz binlerce erişim İSS'si ve birden fazla küresel transit İSS'den oluşan **Ağ Yapısı 2**'ye yol açar. Erişim İSS'leri, fiyatlandırma ve hizmetlerine bağlı olarak rekabet eden küresel transit sağlayıcılar arasından seçim yapabildikleri için Ağ Yapısı 2'yi Ağ Yapısı 1'e kesinlikle tercih ederler. Ancak, küresel transit İSS'lerinin kendilerinin de **birbirine bağlanması** gerektiğini unutmayın: Aksi takdirde, küresel transit sağlayıcılardan birine bağlı olan erişim İSS'leri, diğer küresel transit sağlayıcılara bağlı olan erişim İSS'leri ile iletişim kuramazlardı. Az önce açıklanan Ağ Yapısı 2, en üst katmanda küresel transit sağlayıcıların ve alt katmanda erişim İSS'lerinin bulunduğu **iki katmanlı bir hiyerarşidir**. Bu, küresel transit İSS'lerinin yalnızca her bir erişim İSS'sine yakınlaşmakla kalmayıp aynı zamanda bunu ekonomik olarak da arzu edilir bulduğunu varsayar. Gerçekte, bazı İSS'lerin etkileyici küresel kapsamı olsa ve birçok erişim İSS'si ile doğrudan bağlantı kursa da, hiçbir İSS dünyanın her şehrinde varlığa sahip değildir. Bunun yerine, herhangi bir bölgede, bölgedeki erişim İSS'lerinin bağlandığı bir **bölgesel İSS (regional ISP)** olabilir. Her bölgesel İSS daha sonra **Tier-1 İSS'lerine** bağlanır. Tier-1 İSS'leri bizim (hayali) küresel transit İSS'mize benzer; ancak aslında var olan Tier-1 İSS'lerinin dünyanın her şehrinde varlığı yoktur. Level 3 Communications, AT&T, Sprint ve NTT dahil olmak üzere yaklaşık bir düzine Tier-1 İSS'si bulunmaktadır. İlginç bir şekilde, hiçbir grup resmi olarak Tier-1 statüsünü onaylamaz; derler ki—eğer bir grubun üyesi olup olmadığınızı sormanız gerekiyorsa, muhtemelen değilsinizdir.

Bu ağların ağına dönecek olursak, yalnızca birden fazla rekabet eden Tier-1 İSS'si değil, bir bölgede birden fazla rekabet eden bölgesel İSS de olabilir. Böyle bir hiyerarşide, her erişim İSS'si bağlandığı bölgesel İSS'ye ve her bölgesel İSS bağlandığı Tier-1 İSS'sine ödeme yapar. (Bir erişim İSS'si doğrudan bir Tier-1 İSS'sine de bağlanabilir ve bu durumda Tier-1 İSS'sine ödeme yapar). Dolayısıyla, hiyerarşinin her seviyesinde bir müşteri-sağlayıcı ilişkisi vardır. Tier-1 İSS'lerinin hiyerarşinin en üstünde oldukları için kimseye ödeme yapmadıklarını unutmayın. İşleri daha da karmaşık hale getirmek için, bazı bölgelerde, o bölgedeki daha küçük bölgesel İSS'lerinin bağlandığı daha büyük bir bölgesel İSS (muhtemelen tüm bir ülkeyi kapsayan) olabilir; daha büyük bölgesel İSS daha sonra bir Tier-1 İSS'sine bağlanır. Örneğin, Çin'de her şehirde erişim İSS'leri vardır, bunlar il İSS'lerine, bunlar da ulusal İSS'lerine ve nihayetinde Tier-1 İSS'lerine bağlanır [Tian 2012]. Günümüz internetinin hala kaba bir yaklaşımı olan bu çok katmanlı hiyerarşiye **Ağ Yapısı 3** diyoruz.

Günümüz internetine daha çok benzeyen bir ağ oluşturmak için, hiyerarşik Ağ Yapısı 3'e **varlık noktaları (Points of Presence - PoPs)**, **çoklu bağlantı (multi-homing)**, **eşleme (peering)** ve **internet değişim noktaları (Internet Exchange Points - IXPs)** eklemeliyiz. Varlık noktaları, en alt (erişim İSS'si) seviyesi hariç, hiyerarşinin tüm seviyelerinde bulunur. Bir varlık noktası, sağlayıcının ağında (aynı konumda) bulunan bir veya daha fazla yönlendiriciden oluşan ve müşteri İSS'lerinin sağlayıcı İSS'sine bağlanabileceği bir gruptur. Bir müşteri ağının bir sağlayıcının varlık noktasına bağlanması için, üçüncü taraf bir telekomünikasyon sağlayıcısından yüksek hızlı bir bağlantı kiralayarak yönlendiricilerinden birini doğrudan varlık noktasındaki bir yönlendiriciye bağlayabilir. Herhangi bir İSS (Tier-1 İSS'leri hariç), **çoklu bağlantı** yapmayı, yani iki veya daha fazla sağlayıcı İSS'sine bağlanmayı seçebilir. Örneğin, bir erişim İSS'si iki bölgesel İSS ile çoklu bağlantı yapabileceği gibi, iki bölgesel İSS ve ayrıca bir Tier-1 İSS ile de çoklu bağlantı yapabilir. Benzer şekilde, bir bölgesel İSS birden fazla Tier-1 İSS'si ile çoklu bağlantı yapabilir. Bir İSS çoklu bağlantı yaptığında, sağlayıcılarından birinde bir arıza olsa bile internete paket göndermeye ve almayı sürdürebilir.

Az önce öğrendiğimiz gibi, müşteri İSS'leri küresel internet bağlantısı elde etmek için sağlayıcı İSS'lerine ödeme yapar. Bir müşteri İSS'sinin bir sağlayıcı İSS'sine ödediği miktar, sağlayıcı ile alışveriş yaptığı trafik miktarını yansıtır. Bu maliyetleri azaltmak için, hiyerarşinin aynı seviyesindeki yakındaki iki İSS **eşleme (peer)** yapabilir, yani aralarındaki tüm trafiğin yukarı akış aracıları yerine doğrudan bağlantı üzerinden geçmesi için ağlarını birbirine doğrudan bağlayabilirler. İki İSS eşleme yaptığında, bu genellikle **ücretsiz (settlement-free)** olur, yani hiçbir İSS diğerine ödeme yapmaz. Daha önce belirtildiği gibi, Tier-1 İSS'leri de kendi aralarında ücretsiz olarak eşleme yaparlar. Eşleme ve müşteri-sağlayıcı ilişkileri hakkında okunabilir bir tartışma için [Van der Berg 2008] kaynağına bakınız. Aynı doğrultuda, üçüncü taraf bir şirket, birden fazla İSS'nin birlikte eşleme yapabileceği bir buluşma noktası olan bir **İnternet Değişim Noktası (Internet Exchange Point - IXP)** oluşturabilir. Bir IXP tipik olarak kendi anahtarlarına sahip bağımsız bir binada bulunur [Ager 2012]. Bugün internette 600'den fazla IXP bulunmaktadır [PeeringDB 2020]. Erişim İSS'leri, bölgesel İSS'ler, Tier-1 İSS'leri, varlık noktaları, çoklu bağlantı, eşleme ve IXP'lerden oluşan bu ekosisteme **Ağ Yapısı 4** diyoruz.

Şimdi nihayet günümüz internetini tanımlayan **Ağ Yapısı 5**'e ulaşıyoruz. Ağ Yapısı 5, **içerik sağlayıcı ağlarını (content-provider networks)** ekleyerek Ağ Yapısı 4'ün üzerine inşa edilmiştir. Google şu anda böyle bir içerik sağlayıcı ağının önde gelen örneklerinden biridir. Bu yazının yazıldığı sırada, Google'ın Kuzey Amerika, Avrupa, Asya, Güney Amerika ve Avustralya'ya yayılmış ve her birinde on binlerce veya yüz binlerce sunucuya sahip 19+(tahmini) büyük veri merkezi bulunmaktadır. Ek olarak, Google'ın her birinde birkaç yüz sunucu bulunan daha küçük veri merkezleri de vardır; bu küçük veri merkezleri genellikle IXP'lerin içinde bulunur. Google veri merkezlerinin tümü, tüm dünyayı kapsayan ancak yine de halka açık internetten ayrı olan Google'ın özel TCP/IP ağı üzerinden birbirine bağlıdır. Önemli bir şekilde, Google özel ağı yalnızca Google sunucularına/sunucularından trafik taşır. Mesela Google özel ağı, daha düşük katmanlı İSS'lerle (doğrudan bağlanarak veya IXP'lerde bağlanarak) ücretsiz olarak eşleme yaparak internetin üst katmanlarını "atlamaya" çalışır [Labovitz 2010]. Ancak, birçok erişim İSS'sine hala yalnızca Tier-1 ağları üzerinden geçilerek ulaşılabildiğinden, Google ağı aynı zamanda Tier-1 İSS'lerine de bağlanır ve onlarla alışveriş yaptığı trafik için bu İSS'lere ödeme yapar. Bir içerik sağlayıcı kendi ağını oluşturarak, yalnızca üst katman İSS'lerine yaptığı ödemeleri azaltmakla kalmaz, aynı zamanda hizmetlerinin son kullanıcılara nasıl ulaştırılacağı konusunda da daha fazla kontrole sahip olur. 

Özetle, günümüzün interneti—bir ağlar ağı—karmaşıktır ve bir düzine kadar Tier-1 İSS'si ve yüz binlerce alt katman İSS'sinden oluşur. İSS'ler kapsam açısından çeşitlidir; bazıları birden fazla kıtayı ve okyanusu kapsarken, diğerleri dar coğrafi bölgelerle sınırlıdır. Alt katman İSS'leri üst katman İSS'lerine bağlanır ve üst katman İSS'leri birbirleriyle bağlantı kurar. Kullanıcılar ve içerik sağlayıcılar alt katman İSS'lerinin müşterileridir ve alt katman İSS'leri üst katman İSS'lerinin müşterileridir. Son yıllarda, büyük içerik sağlayıcılar da kendi ağlarını oluşturmuş ve mümkün olduğunca doğrudan alt katman İSS'lerine bağlanmışlardır.

#### Paket Anahtarlamalı Ağlarda Gecikme, Kayıp ve Verim

Geçen bölümlerde internetin, uç sistemlerde çalışan dağıtılmış uygulamalara hizmet sağlayan bir altyapı olarak görülebileceğini söylemiştik. 
İdeal olarak, internet hizmetlerinin herhangi iki uç sistem arasında istediğimiz kadar veriyi anında ve veri kaybı olmadan taşıyabilmesini isteriz. 
Ne yazık ki, bu yüksek bir hedef ve gerçekte ulaşılması mümkün değil. 
Bunun yerine, bilgisayar ağları zorunlu olarak uç sistemler arasındaki **verimi (throughput)** (saniyede aktarılabilecek veri miktarı) sınırlar, uç sistemler arasında **gecikmelere (delays)** neden olur ve aslında **paketleri kaybedebilir (lose packets)**.

Bir yandan, gerçekliğin fiziksel yasalarının gecikme ve kayıplara neden olması ve verimi sınırlaması üzücü bir durumdur. 
Öte yandan, bilgisayar ağlarında bu sorunlar olduğu için, bu sorunlarla nasıl başa çıkılacağı konusunda pek çok büyüleyici konu vardır—
bilgisayar ağları üzerine bir dersi doldurmaya ve binlerce doktora tezini motive etmeye yetecek kadar çok konu! 
Bu bölümde, bilgisayar ağlarındaki gecikmeyi, kaybı ve verimi incelemeye ve ölçmeye başlayacağız.

#### Paket Anahtarlamalı Ağlarda Gecikmeye Genel Bakış

Hatırlayacağınız gibi, bir paket bir ana bilgisayarda (kaynak) başlar, bir dizi yönlendiriciden (router) geçer ve yolculuğunu başka bir ana bilgisayarda (hedef) sonlandırır. Bir paket bu yol boyunca bir düğümden(nodec) (ana bilgisayar veya yönlendirici) sonraki düğüme (ana bilgisayar veya yönlendirici) giderken, yol üzerindeki her düğümde çeşitli **gecikmeler** yaşar. Bu gecikmelerin en önemlileri şunlardır: **düğüm işleme gecikmesi (nodal processing delay)**, **kuyruk gecikmesi (queuing delay)**, **iletim gecikmesi (transmission delay)** ve **yayılma gecikmesi (propagation delay)**. Bu gecikmelerin tümü bir araya gelerek **toplam düğüm gecikmesini**(total nodal delay) oluşturur.

Arama, Web'de gezinme, e-posta, haritalar, anlık mesajlaşma ve **VoIP (voice-over-IP)** gibi birçok internet uygulamasının performansı, ağ gecikmelerinden büyük ölçüde etkilenir. Paket anahtarlama ve bilgisayar ağlarını derinlemesine anlamak için, bu gecikmelerin doğasını ve önemini kavramamız gerekir.

#### Gecikme Türleri

Şimdi örneklemek istiyorum, kaynak ve hedef arasındaki uçtan uca rotasının bir parçası olarak, bir paket yukarı akış düğümünden yönlendirici A aracılığıyla yönlendirici B'ye gönderiliyor diyelim. Amacımız, yönlendirici A'daki düğüm gecikmesini karakterize etmektir. Yönlendirici A'nın yönlendirici B'ye giden bir **giden bağlantısı (outbound link)** olduğunu unutmayın. Bu bağlantının önünde bir **kuyruk (queue)** (ayrıca **tampon (buffer)** olarak da bilinir) bulunur. Paket yukarı akış düğümünden yönlendirici A'ya ulaştığında, yönlendirici A paketin başlığını (packet's header) inceleyerek paket için uygun giden bağlantıyı belirler ve ardından paketi bu bağlantıya yönlendirir. Bu örnekte, paketin giden bağlantısı yönlendirici B'ye giden bağlantıdır. Bir paket bir bağlantı üzerinden ancak o anda bağlantı üzerinde başka bir paket iletilmiyorsa ve kuyrukta kendisinden önce başka paket yoksa iletilebilir; bağlantı o anda meşgulse veya bağlantı için zaten kuyrukta bekleyen başka paketler varsa, yeni gelen paket kuyruğa katılır.

#### İşleme Gecikmesi (Processing Delay)

Paketin başlığının (packet's header) incelenmesi ve paketin nereye yönlendirileceğinin belirlenmesi için gereken süre, **işleme gecikmesinin** bir parçasıdır. İşleme gecikmesi, paketin bitlerinin yukarı akış düğümünden yönlendirici A'ya iletilmesi sırasında meydana gelen bit seviyesindeki hataların kontrol edilmesi için gereken süre gibi başka faktörleri de içerebilir. Yüksek hızlı yönlendiricilerdeki işleme gecikmeleri genellikle **mikrosaniye** veya daha az mertebededir. Bu düğüm işlemesinden sonra, yönlendirici paketi yönlendirici B'ye giden bağlantının önündeki kuyruğa yönlendirir.

#### Kuyruk Gecikmesi (Queuing Delay)

Paket, kuyrukta bağlantı üzerinden iletilmeyi beklerken bir **kuyruk gecikmesi** yaşar. Belirli bir paketin kuyruk gecikmesinin uzunluğu, kuyrukta bekleyen ve bağlantı üzerinden iletilmeyi bekleyen daha önce gelen paketlerin sayısına bağlı olacaktır. Kuyruk boşsa ve o anda başka bir paket iletilmiyorsa, paketimizin kuyruk gecikmesi sıfır olacaktır. Öte yandan, trafik yoğunsa ve birçok başka paket de iletilmeyi bekliyorsa, kuyruk gecikmesi uzun olacaktır. Kısa bir süre sonra, gelen bir paketin bulmayı bekleyebileceği paket sayısının, kuyruğa gelen trafiğin yoğunluğunun ve doğasının bir fonksiyonu olduğunu göreceğiz. Kuyruk gecikmeleri pratikte **mikrosaniyelerden milisaniyelere** kadar değişebilir.

#### İletim Gecikmesi (Transmission Delay)

Paketlerin, paket anahtarlamalı ağlarda yaygın olduğu gibi, ilk gelene ilk hizmet (first-come-first-served) prensibine göre iletildiğini varsayarsak, paketimiz ancak kendisinden önce gelen tüm paketler iletildikten sonra iletilebilir. Paketin uzunluğunu L bit ile ve yönlendirici A'dan yönlendirici B'ye olan bağlantının **iletim hızını (transmission rate)** R bit/sn ile gösterelim. Örneğin, 10 Mbps Ethernet bağlantısı için hız `R = 10 Mbps'dir`; 100 Mbps Ethernet bağlantısı için hız `R = 100 Mbps'dir`. **İletim gecikmesi L/R**'dir. Bu, paketin tüm bitlerini bağlantıya itmek (yani, iletmek) için gereken süredir. İletim gecikmeleri pratikte genellikle **mikrosaniyelerden milisaniyelere** kadar değişebilir.

#### Yayılma Gecikmesi (Propagation Delay)

Bir bit bağlantıya itildikten sonra, yönlendirici B'ye **yayılması (propagate)** gerekir. Bağlantının başından yönlendirici B'ye yayılmak için gereken süreye **yayılma gecikmesi** denir. Bit, bağlantının **yayılma hızında (propagation speed)** yayılır. Yayılma hızı, bağlantının fiziksel ortamına (yani, fiber optik, bükümlü çift bakır tel vb.) bağlıdır ve şu aralıktadır:

`2 çarpı 10 üzeri 8 metre/sn ile 3 çarpı 10 üzeri 8 metre/sn`

bu da ışık hızına eşit veya biraz daha azdır. Yayılma gecikmesi, iki yönlendirici arasındaki mesafenin yayılma hızına bölünmesiyle bulunur. Yani, yayılma gecikmesi d/s'dir; burada d, yönlendirici A ile yönlendirici B arasındaki mesafedir ve s, bağlantının yayılma hızıdır. Paketin son biti düğüm B'ye ulaştığında, o ve paketin önceki tüm bitleri yönlendirici B'de saklanır. Tüm süreç daha sonra yönlendirici B'nin yönlendirme işlemini gerçekleştirmesiyle devam eder. Geniş alan ağlarında (wide-area networks), yayılma gecikmeleri **milisaniyeler** mertebesindedir.

#### İletim ve Yayılma Gecikmesini Karşılaştırma

Bilgisayar ağı alanına yeni girenler bazen iletim gecikmesi ile yayılma gecikmesi arasındaki farkı anlamakta zorluk çekerler. Bu fark ince ama önemlidir. İletim gecikmesi, yönlendiricinin paketi dışarı itmesi için gereken süredir; paketin uzunluğunun ve bağlantının iletim hızının bir fonksiyonudur, ancak iki yönlendirici arasındaki mesafeyle hiçbir ilgisi yoktur. Yayılma gecikmesi ise bir bitin bir yönlendiriciden diğerine yayılması için geçen süredir; iki yönlendirici arasındaki mesafenin bir fonksiyonudur, ancak paketin uzunluğu veya bağlantının iletim hızıyla hiçbir ilgisi yoktur.

Bir benzetme, iletim ve yayılma gecikmesi kavramlarını netleştirebilir. Örneğin, her 100 kilometrede bir gişesi olan bir otoyol düşünün. Gişeler arasındaki otoyol bölümlerini bağlantılar ve gişeleri yönlendiriciler olarak düşünebilirsiniz. Arabaların otoyolda 100 km/saat hızla hareket ettiğini (yani, bir araba bir gişeden çıktığında anında 100 km/saat hıza ulaştığını ve gişeler arasında bu hızı koruduğunu) varsayalım. Ardından, 10 arabanın sabit bir sırada birbirini takip eden bir konvoy halinde birlikte seyahat ettiğini varsayalım. Her arabayı bir bit ve konvoyu bir paket olarak düşünebilirsiniz. Ayrıca, her gişenin bir arabaya 12 saniyede hizmet verdiğini (yani, ilettiğini) ve gecenin geç saatleri olduğunu, bu nedenle konvoydaki arabaların otoyoldaki tek arabalar olduğunu varsayalım. Son olarak, konvoydaki ilk araba bir gişeye ulaştığında, diğer dokuz araba gelip arkasında sıralanana kadar girişte beklediğini varsayalım. (Yani, tüm konvoy iletilmeye başlanmadan önce gişede depolanmalıdır.)

Gişenin tüm konvoyu otoyola itmesi için gereken süre (10 araba) / (5 araba/dakika) = 2 dakikadır. Bu süre, bir yönlendiricideki iletim gecikmesine benzerdir. Bir arabanın bir gişenin çıkışından bir sonraki gişenin çıkışına gitmesi için gereken süre 100 km / (100 km/saat) = 1 saattir. Bu süre, yayılma gecikmesine benzerdir. Bu nedenle, konvoyun bir gişenin önünde depolandığı andan bir sonraki gişenin önünde depolandığı ana kadar geçen süre, iletim gecikmesi ile yayılma gecikmesinin toplamıdır—bu örnekte 62 dakika. Bu benzetmeyi biraz daha inceleyelim. Bir konvoy için gişe hizmet süresi, bir arabanın gişeler arasında seyahat etme süresinden daha uzun olsaydı ne olurdu? Örneğin, şimdi arabaların 1000 km/saat hızla seyahat ettiğini ve gişenin dakikada bir arabaya hizmet verdiğini varsayalım. Bu durumda, iki gişe arasındaki seyahat gecikmesi 6 dakika ve bir konvoya hizmet etme süresi 10 dakikadır. Bu durumda, konvoydaki ilk birkaç araba, konvoydaki son arabalar ilk gişeden ayrılmadan ikinci gişeye ulaşacaktır. Bu durum paket anahtarlamalı ağlarda da ortaya çıkar—bir paketteki ilk bitler bir yönlendiriciye ulaşabilirken, paketteki birçok bit hala önceki yönlendirici tarafından iletilmeyi bekliyor olabilir.

Eğer işleme, kuyruk, iletim ve yayılma gecikmelerini sırasıyla d<sub>proc</sub>, d<sub>queue</sub>, d<sub>trans</sub> ve d<sub>prop</sub> ile gösterirsek, toplam düğüm gecikmesi şu şekilde verilir:

d<sub>nodal</sub> = d<sub>proc</sub> + d<sub>queue</sub> + d<sub>trans</sub> + d<sub>prop</sub>

Bu gecikme bileşenlerinin katkısı önemli ölçüde değişebilir. Örneğin, aynı üniversite kampüsündeki iki yönlendiriciyi birbirine bağlayan bir bağlantı için d<sub>prop</sub> ihmal edilebilir (örneğin, birkaç mikrosaniye); ancak, jeostatik bir uydu bağlantısıyla birbirine bağlanan iki yönlendirici için d<sub>prop</sub> yüzlerce milisaniye olabilir ve d<sub>nodal</sub> içindeki baskın terim olabilir. Benzer şekilde, d<sub>trans</sub> ihmal edilebilir düzeyden önemli düzeye kadar değişebilir. Katkısı tipik olarak 10 Mbps ve üzeri iletim hızları için (örneğin, LAN'lar için) ihmal edilebilir düzeydedir; ancak, düşük hızlı dial-up modem bağlantıları üzerinden gönderilen büyük internet paketleri için yüzlerce milisaniye olabilir. İşleme gecikmesi olan d<sub>proc</sub> genellikle ihmal edilebilir düzeydedir; ancak, bir yönlendiricinin paketleri iletebileceği maksimum hız olan yönlendiricinin maksimum verimini güçlü bir şekilde etkiler.

#### Kuyruk Gecikmesi ve Paket Kaybı

Düğüm gecikmesinin en karmaşık ve ilginç bileşeni kuyruk gecikmesidir (d<sub>queue</sub>). Aslında, kuyruk gecikmesi bilgisayar ağlarında o kadar önemli ve ilgi çekicidir ki, bu konuda binlerce makale ve sayısız kitap yazılmıştır [Bertsekas 1991; Kleinrock 1975, Kleinrock 1976]. Burada kuyruk gecikmesi hakkında yalnızca üst düzey, sezgisel bir tartışma sunacağız; daha meraklı okuyucu bazı kitaplara göz atmak (hatta sonunda bu konuda bir doktora tezi yazmak bile) isteyebilir! Diğer üç gecikmeden (yani, d<sub>proc</sub>, d<sub>trans</sub> ve d<sub>prop</sub>) farklı olarak, kuyruk gecikmesi paketten pakete değişebilir. Örneğin, boş bir kuyruğa aynı anda 10 paket gelirse, ilk iletilen paket hiç kuyruk gecikmesi yaşamazken, son iletilen paket nispeten büyük bir kuyruk gecikmesi yaşayacaktır (diğer dokuz paketin iletilmesini beklerken). Bu nedenle, kuyruk gecikmesini karakterize ederken, genellikle ortalama kuyruk gecikmesi, kuyruk gecikmesinin varyansı ve kuyruk gecikmesinin belirli bir değeri aşma olasılığı gibi istatistiksel ölçüler kullanılır.

Kuyruk gecikmesi ne zaman büyük ve ne zaman önemsizdir? Bu sorunun cevabı, trafiğin kuyruğa geliş hızına, bağlantının iletim hızına ve gelen trafiğin doğasına, yani trafiğin periyodik olarak mı yoksa patlamalar halinde mi geldiğine bağlıdır. Burada biraz fikir edinmek için, a'nın paketlerin kuyruğa ortalama geliş hızını (a, paket/sn birimindedir) gösterdiğini varsayalım. R'nin iletim hızı olduğunu hatırlayın; yani, bitlerin kuyruktan dışarı itildiği hızdır (bit/sn biriminde). Ayrıca, basitlik için tüm paketlerin L bit içerdiğini varsayalım. O zaman bitlerin kuyruğa ortalama geliş hızı La bit/sn'dir. Son olarak, kuyruğun çok büyük olduğunu, yani esasen sonsuz sayıda bit tutabileceğini varsayalım. **Trafik yoğunluğu** olarak adlandırılan La/R oranı, kuyruk gecikmesinin boyutunu tahmin etmede genellikle önemli bir rol oynar. La/R > 1 ise, bitlerin kuyruğa ortalama geliş hızı, bitlerin kuyruktan iletilebileceği hızı aşar. Bu talihsiz durumda, kuyruk sınırsız bir şekilde artma eğiliminde olacak ve kuyruk gecikmesi sonsuza yaklaşacaktır! Bu nedenle, trafik mühendisliğindeki altın kurallardan biri şudur: Sisteminizi trafik yoğunluğu 1'den büyük olmayacak şekilde tasarlayın.

Şimdi La/R ≤ 1 durumunu ele alalım. Burada, gelen trafiğin doğası kuyruk gecikmesini etkiler. Örneğin, paketler periyodik olarak gelirse—yani, her L/R saniyede bir paket gelirse—o zaman her paket boş bir kuyruğa ulaşacak ve hiçbir kuyruk gecikmesi olmayacaktır. Öte yandan, paketler patlamalar halinde ancak periyodik olarak gelirse, önemli bir ortalama kuyruk gecikmesi olabilir. Örneğin, her (L/R)N saniyede bir N paket aynı anda geldiğini varsayalım. O zaman ilk iletilen paketin kuyruk gecikmesi yoktur; ikinci iletilen paketin kuyruk gecikmesi L/R saniyedir; ve daha genel olarak, n'inci iletilen paketin kuyruk gecikmesi (n - 1)L/R saniyedir. Bu örnekteki ortalama kuyruk gecikmesini hesaplamak size bir alıştırma olarak bırakılmıştır.

Yukarıda açıklanan periyodik gelişlerin iki örneği biraz akademiktir. Tipik olarak, bir kuyruğa geliş süreci rastgeledir; yani, gelişler herhangi bir örüntü izlemez ve paketler rastgele zaman aralıklarıyla ayrılır. Bu daha gerçekçi durumda, La/R miktarı genellikle kuyruk gecikmesi istatistiklerini tam olarak karakterize etmek için yeterli değildir. Bununla birlikte, kuyruk gecikmesinin boyutunu sezgisel olarak anlamak için faydalıdır. Özellikle, trafik yoğunluğu sıfıra yakınsa, paket gelişleri seyrek ve aralıklıdır ve gelen bir paketin kuyrukta başka bir paket bulması olası değildir. Bu nedenle, ortalama kuyruk gecikmesi sıfıra yakın olacaktır. Öte yandan, trafik yoğunluğu 1'e yakın olduğunda, geliş hızının iletim kapasitesini aştığı zaman aralıkları (paket geliş hızındaki değişimler nedeniyle) olacaktır ve bu süre zarfında bir kuyruk oluşacaktır; geliş hızı iletim kapasitesinden daha az olduğunda, kuyruğun uzunluğu küçülecektir. Yine de, trafik yoğunluğu 1'e yaklaştıkça, ortalama kuyruk uzunluğu giderek büyür. 

#### Paket Kaybı

Yukarıdaki tartışmalarımızda, kuyruğun sonsuz sayıda paket tutabileceğini varsaydık. Gerçekte, bir bağlantının önündeki bir kuyruk sınırlı kapasiteye sahiptir, ancak kuyruk kapasitesi büyük ölçüde yönlendirici tasarımına ve maliyetine bağlıdır. Kuyruk kapasitesi sınırlı olduğundan, trafik yoğunluğu 1'e yaklaşırken paket gecikmeleri gerçekten sonsuza yaklaşmaz. Bunun yerine, bir paket dolu bir kuyruğa ulaşabilir. Böyle bir paketi saklayacak yer olmadığından, bir yönlendirici o paketi düşürecektir; yani, paket kaybolacaktır. Trafik yoğunluğu 1'den büyük olduğunda bu kuyruk taşması etkileşimli animasyonda tekrar görülebilir.

Bir uç sistem açısından, bir paket kaybı, ağ çekirdeğine iletilmiş ancak hedefteki ağdan asla çıkmamış gibi görünecektir. Kaybolan paketlerin oranı, trafik yoğunluğu arttıkça artar. Bu nedenle, bir düğümdeki performans genellikle yalnızca gecikme açısından değil, aynı zamanda paket kaybı olasılığı açısından da ölçülür. Sonraki bölümlerde tartışacağımız gibi, tüm verilerin sonunda kaynaktan hedefe aktarılmasını sağlamak için kaybolan bir paket uçtan uca bazda yeniden iletilebilir.

#### Uçtan Uca Gecikme (End-to-End Delay)

Bu noktaya kadar olan tartışmamız düğüm gecikmesine, yani tek bir yönlendiricideki gecikmeye odaklandı. Şimdi de kaynaktan hedefe olan toplam gecikmeyi ele alalım. Bu kavramı anlamak için, kaynak ana bilgisayar ile hedef ana bilgisayar arasında N - 1 adet yönlendirici olduğunu varsayalım. Ayrıca, şimdilik ağın sıkışık olmadığını (böylece kuyruk gecikmelerinin ihmal edilebilir olduğunu), her yönlendiricide ve kaynak ana bilgisayarda işleme gecikmesinin d<sub>proc</sub> olduğunu, her yönlendiriciden ve kaynak ana bilgisayardan çıkan iletim hızının R bit/sn olduğunu ve her bağlantıdaki yayılmanın d<sub>prop</sub> olduğunu varsayalım. Düğüm gecikmeleri birikerek uçtan uca gecikmeyi verir:

d<sub>uçtan-uca</sub> = N ⋅ (d<sub>proc</sub> + d<sub>trans</sub> + d<sub>prop</sub>)  

Burada, tekrar belirtmek gerekirse, d<sub>trans</sub> = L/R'dir ve L paket boyutudur. 

#### Traceroute

Bir bilgisayar ağındaki uçtan uca gecikmeyi uygulamalı olarak deneyimlemek için Traceroute programını kullanabiliriz. Traceroute, herhangi bir internet ana bilgisayarında çalışabilen basit bir programdır. Kullanıcı bir hedef ana bilgisayar adı (hostname) belirttiğinde, kaynak ana bilgisayardaki program bu hedefe doğru birden fazla özel paket gönderir. Bu paketler hedefe doğru ilerlerken bir dizi yönlendiriciden geçerler. Bir yönlendirici bu özel paketlerden birini aldığında, kaynağa yönlendiricinin adını ve adresini içeren kısa bir mesaj geri gönderir.

Daha spesifik olarak, kaynak ile hedef arasında N - 1 adet yönlendirici olduğunu varsayalım. Kaynak daha sonra ağa, her biri nihai hedefe adreslenmiş N adet özel paket gönderecektir. Bu N özel paket 1'den N'ye kadar numaralandırılır, ilk paket 1 ve son paket N olarak işaretlenir. n'inci yönlendirici, n olarak işaretlenmiş n'inci paketi aldığında, yönlendirici paketi hedefine doğru iletmez, bunun yerine kaynağa bir mesaj geri gönderir. Hedef ana bilgisayar N'inci paketi aldığında, o da kaynağa bir mesaj geri gönderir.

Kaynak, bir paket gönderdiği zaman ile karşılık gelen dönüş mesajını aldığı zaman arasındaki süreyi kaydeder; ayrıca mesajı döndüren yönlendiricinin (veya hedef ana bilgisayarın) adını ve adresini de kaydeder. Bu şekilde, kaynak, paketlerin kaynaktan hedefe akarken izlediği yolu yeniden oluşturabilir ve kaynak, tüm ara yönlendiricilere olan gidiş-dönüş gecikmelerini belirleyebilir. Traceroute aslında az önce açıklanan deneyi üç kez tekrarlar, bu nedenle kaynak aslında hedefe 3 ⋅ N paket gönderir.  RFC 1393, Traceroute'u ayrıntılı olarak açıklamaktadır. 

İşte Traceroute programının bir çıktı örneği; burada rota, benim kaynağımdan Google DNS sunucusuna (8.8.8.8) yapılmıştır.

Çıktı altı sütuna sahiptir: birinci sütun yukarıda açıklanan n değeridir, yani rotadaki yönlendiricinin numarası; ikinci sütun yönlendiricinin adıdır; üçüncü sütun yönlendiricinin adresidir (xxx.xxx.xxx.xxx biçiminde); son üç sütun ise üç deney için gidiş-dönüş gecikmeleridir. Kaynak herhangi bir yönlendiriciden üçten az mesaj alırsa (ağdaki paket kaybı nedeniyle), Traceroute yönlendirici numarasının hemen yanına bir yıldız işareti koyar ve o yönlendirici için üçten az gidiş-dönüş süresi bildirir.

![resim](https://i.ibb.co/vCX3SRRK/Trace-Route-Google.png)

Kaynak ile hedef arasında 11 yönlendirici bulunmaktadır (sonuncusu hedef). Bu yönlendiricilerin bazılarının adı varken, hepsinin adresleri vardır. Örneğin, 1. Yönlendiricinin adı HUAWEI-COMPUTER.mshome.net ve adresi 172.19.112.1'dir. Bu yönlendirici için sağlanan verilere baktığımızda, üç denemenin ilkinde kaynak ile yönlendirici arasındaki gidiş-dönüş gecikmesinin 0.690 ms olduğunu görüyoruz. Sonraki iki deneme için gidiş-dönüş gecikmeleri 0.512 ve 0.444 ms idi.

İkinci hop'ta (192.168.1.1) bir denemede zaman aşımı yaşanmış (asterisk ile belirtilmiş). Üçüncü hop'ta (195.87.128.29) gidiş-dönüş gecikmeleri sırasıyla 17.520 ms, 17.448 ms ve 17.355 ms olarak ölçülmüş. Dördüncü hop'ta ise üç denemede de yanıt alınamamış.

Beşinci hop'ta (84.44.91.157) gecikmeler 27.157 ms, 37.057 ms ve 27.109 ms olarak kaydedilmiş. Altıncı hop'ta (10.135.50.250) ise 36.997 ms, 33.941 ms ve 33.909 ms değerleri görülüyor. Yedinci hop'ta (ae3-17-xcr1.ise.cw.net) gecikmeler 33.894 ms, 18.600 ms ve 18.561 ms olarak ölçülmüş. Burada "ise" ifadesi, bu yönlendiricinin İstanbul'da olabileceğini düşündürüyor.

Sekizinci hop'ta (ae29-xcr1.sof.cw.net) gecikmeler 38.561 ms, 28.919 ms ve 28.888 ms olarak kaydedilmiş. "sof" ifadesi ise bu yönlendiricinin Sofya'da olabileceğine işaret ediyor, bu da Türkiye'den sonra bir yurt dışı geçiş olduğunu gösteriyor. Dokuzuncu hop'ta ilk denemede zaman aşımı yaşanmış, sonraki iki denemede ise farklı Google IP adreslerine (209.85.168.146 ve 209.85.149.140) ulaşılmış, bu da yük dengelemesi veya farklı yönlendirme yollarının olabileceğini gösteriyor. Onuncu hop'ta ise üç denemede de yanıt alınamamış.

Son olarak, on birinci hop'ta hedefe (dns.google, yani 8.8.8.8) ulaşılmış ve gecikmeler 39.497 ms, 39.558 ms ve 39.408 ms olarak ölçülmüş. Burada da farklı bir Google IP adresi (72.14.237.137) gözlemleniyor.

Bu gidiş-dönüş gecikmeleri, iletim gecikmeleri, yayılma gecikmeleri, yönlendirici işleme gecikmeleri ve kuyruk gecikmesi dahil olmak üzere az önce tartışılan tüm gecikmeleri içerir. Kuyruk gecikmesi zamanla değiştiği için, farklı denemelerde farklı gecikme süreleri gözlemlenmiştir. Ayrıca, bazı hop'larda yaşanan zaman aşımları (asteriskler), o yönlendiricilere ulaşmada sorunlar yaşandığını veya o yönlendiricilerin ICMP yanıtlarını engellediğini gösterebilir. Özellikle 7. ve 8. yönlendiriciler arasındaki gecikme artışı, Türkiye ile Bulgaristan arasındaki olası bir fiber optik bağlantıdan kaynaklanan nispeten büyük bir yayılma gecikmesine işaret edebilir.

#### Uç Sistem, Uygulama ve Diğer Gecikmeler

İşleme, iletim ve yayılma gecikmelerine ek olarak, uç sistemlerde de önemli ek gecikmeler olabilir. 
Örneğin, paylaşılan bir ortama (örneğin, WiFi veya kablo modem senaryosunda olduğu gibi) bir paket iletmek isteyen bir uç sistem, ortamı diğer uç sistemlerle paylaşma protokolünün bir parçası olarak iletimini kasıtlı olarak geciktirebilir.

Bir diğer önemli gecikme ise **medya paketleme gecikmesidir (media packetization delay)** ve bu gecikme **Voice-over-IP (VoIP)** uygulamalarında bulunur. 
VoIP'te, gönderen taraf paketi internete göndermeden önce şifrelenmiş dijital konuşma ile doldurmalıdır. 
Bir paketi doldurmak için geçen bu süreye **paketleme gecikmesi (packetization delay)** denir ve bu süre önemli olabilir ve bir VoIP görüşmesinin kullanıcı tarafından algılanan kalitesini etkileyebilir.

#### Bilgisayar Ağlarında Verim (Throughput)

Gecikme ve paket kaybına ek olarak, bilgisayar ağlarındaki bir diğer kritik performans ölçütü uçtan uca verimdir. 
Verimi tanımlamak için, bir bilgisayar ağı üzerinden Ana Bilgisayar A'dan Ana Bilgisayar B'ye büyük bir dosya aktarımını düşünün. 
Bu aktarım, örneğin bir bilgisayardan diğerine büyük bir video klip olabilir. 
Herhangi bir anda anlık verim, Ana Bilgisayar B'nin dosyayı aldığı orandır (bit/sn cinsinden). (Birçok uygulama, indirmeler sırasında kullanıcı arayüzünde anlık verimi görüntüler—belki bunu daha önce gözlemlemişsinizdir! Speedtest uygulamasını [Speedtest 2025] kullanarak kendi bilgisayarınız ile internetteki sunucular arasındaki uçtan uca gecikmeyi ve indirme verimini ölçmek isteyebilirsiniz.) Dosya F bit içeriyorsa ve Ana Bilgisayar B'nin tüm F bitini alması T saniye sürüyorsa, dosya aktarımının ortalama verimi F/T bit/sn'dir. İnternet telefon görüşmeleri gibi bazı uygulamalar için düşük gecikme ve anlık verimin sürekli olarak belirli bir eşiğin üzerinde olması (örneğin, bazı internet telefon görüşmeleri uygulamaları için 24 kbps'nin üzerinde ve bazı gerçek zamanlı video uygulamaları için 256 kbps'nin üzerinde) arzu edilir. Dosya aktarımlarını içerenler de dahil olmak üzere diğer uygulamalar için gecikme kritik değildir, ancak mümkün olan en yüksek verime sahip olmak arzu edilir.

Verim kavramını daha iyi anlamak için birkaç örnek ele alalım. Örneğin, iki iletişim bağlantısı ve bir yönlendirici ile birbirine bağlı iki uç sistemi, bir sunucu ve bir istemci var. Sunucudan istemciye bir dosya aktarımı için verimi düşünün. R<sub>s</sub>, sunucu ile yönlendirici arasındaki bağlantının hızını; R<sub>c</sub> ise yönlendirici ile istemci arasındaki bağlantının hızını göstersin. Tüm ağda gönderilen tek bitlerin sunucudan istemciye giden bitler olduğunu varsayalım. Şimdi bu ideal senaryoda sunucudan istemciye olan verimin ne olduğunu soruyoruz. Bu soruyu cevaplamak için bitleri sıvı ve iletişim bağlantılarını borular olarak düşünebiliriz. Açıkça görülüyor ki, sunucu kendi bağlantısından R<sub>s</sub> bps'den daha hızlı bir oranda bit pompalayamaz; ve yönlendirici de R<sub>c</sub> bps'den daha hızlı bir oranda bitleri iletemez. Eğer R<sub>s</sub> ≤ R<sub>c</sub> ise, sunucu tarafından pompalanan bitler yönlendiriciden "akıp" geçecek ve istemciye R<sub>s</sub> bps hızında ulaşacak, bu da R<sub>s</sub> bps'lik bir verim sağlayacaktır. Öte yandan, eğer R<sub>c</sub> ≤ R<sub>s</sub> ise, yönlendirici bitleri aldığı kadar hızlı iletemeyecektir. Bu durumda, bitler yalnızca R<sub>c</sub> hızında yönlendiriciden ayrılacak ve uçtan uca verim R<sub>c</sub> olacaktır. (Ayrıca, bitlerin R<sub>s</sub> hızında yönlendiriciye gelmeye ve R<sub>c</sub> hızında yönlendiriciden ayrılmaya devam etmesi durumunda, istemciye iletilmeyi bekleyen bitlerin yönlendiricide birikmeye devam edeceğini de unutmayın—bu çok istenmeyen bir durumdur!) Bu nedenle, bu basit iki bağlantılı ağ için verim min{R<sub>c</sub>, R<sub>s</sub>}'dir, yani darboğaz bağlantısının iletim hızıdır. Verimi belirledikten sonra, F bitlik büyük bir dosyanın sunucudan istemciye aktarılmasının ne kadar süreceğini F/min{R<sub>s</sub>, R<sub>c</sub>} olarak yaklaşık olarak hesaplayabiliriz. Belirli bir örnek için, F = 32 milyon bitlik bir MP3 dosyası indirdiğinizi, sunucunun iletim hızının R<sub>s</sub> = 2 Mbps ve sizin erişim bağlantınızın hızının R<sub>c</sub> = 1 Mbps olduğunu varsayalım. Dosyanın aktarılması için gereken süre o zaman 32 saniyedir. Elbette, verim ve aktarım süresi için bu ifadeler yalnızca birer yaklaşımdır, çünkü sakla-ve-ilet (store-and-forward) ve işleme gecikmelerinin yanı sıra protokol sorunlarını da hesaba katmazlar.

Şimdi sunucu ile istemci arasında iletim hızları R<sub>1</sub>, R<sub>2</sub>, ..., R<sub>N</sub> olan N bağlantılı bir ağ olsun. 
İki bağlantılı ağ için yapılan aynı analizi uygulayarak, sunucudan istemciye bir dosya aktarımı için verimin min{R<sub>1</sub>, R<sub>2</sub>, ..., R<sub>N</sub>} olduğunu buluruz, bu da yine sunucu ile istemci arasındaki yoldaki darboğaz bağlantısının iletim hızıdır.

Şimdi günümüz internetinden esinlenen başka bir örnek ele alalım. Bir bilgisayar ağına bağlı iki uç sistem, bir sunucu ve bir istemci olsun. 
Sunucudan istemciye bir dosya aktarımı için verimi düşünün. Sunucu, R<sub>s</sub> hızında bir erişim bağlantısıyla ağa bağlıdır ve istemci de R<sub>c</sub> hızında bir erişim bağlantısıyla ağa bağlıdır. Şimdi, iletişim ağının çekirdeğindeki tüm bağlantıların R<sub>s</sub> ve R<sub>c</sub>'den çok daha yüksek, çok yüksek iletim hızlarına sahip olduğunu varsayalım. Gerçekten de, bugün internetin çekirdeği, çok az tıkanıklık yaşayan yüksek hızlı bağlantılarla aşırı tahsis edilmiştir (over-provisioned). Ayrıca, tüm ağda gönderilen tek bitlerin sunucudan istemciye giden bitler olduğunu varsayalım. Bu örnekte bilgisayar ağının çekirdeği geniş bir boru gibi olduğundan, bitlerin kaynaktan hedefe akabileceği hız yine R<sub>s</sub> ve R<sub>c</sub>'nin minimumudur, yani verim = min{R<sub>s</sub>, R<sub>c</sub>}. Bu nedenle, günümüz internetinde verim için kısıtlayıcı faktör tipik olarak erişim ağıdır.

Son bir örnek için, düşünün; burada bilgisayar ağının çekirdeğine bağlı 10 sunucu ve 10 istemci bulunmaktadır. 
Bu örnekte, 10 istemci-sunucu çiftini içeren 10 eş zamanlı indirme işlemi gerçekleşmektedir. 
Bu 10 indirmenin şu anda ağdaki tek trafik olduğunu varsayalım. Çekirdekteki tüm 10 indirme tarafından geçilen bir bağlantı bulunsun. 
Bu bağlantının iletim hızını R ile gösterelim. Tüm sunucu erişim bağlantılarının aynı R<sub>s</sub> hızına, tüm istemci erişim bağlantılarının aynı R<sub>c</sub> hızına ve R hızındaki ortak bağlantı dışındaki çekirdekteki tüm bağlantıların iletim hızlarının R<sub>s</sub>, R<sub>c</sub> ve R'den çok daha büyük olduğunu varsayalım. Şimdi soruyoruz, indirmelerin verimleri nelerdir? Açıkçası, ortak bağlantının hızı R büyükse—diyelim ki hem R<sub>s</sub> hem de R<sub>c</sub>'den yüz kat daha büyükse—o zaman her indirme için verim yine min{R<sub>s</sub>, R<sub>c</sub>} olacaktır. 
Peki ya ortak bağlantının hızı R<sub>s</sub> ve R<sub>c</sub> ile aynı mertebedeyse? Bu durumda verim ne olacaktır? Belirli bir örneğe bakalım. 
R<sub>s</sub> = 2 Mbps, R<sub>c</sub> = 1 Mbps, R = 5 Mbps ve ortak bağlantının iletim hızını 10 indirme arasında eşit olarak paylaştırdığını varsayalım. O zaman her indirme için darboğaz artık erişim ağında değil, bunun yerine her indirmeye yalnızca 500 kbps verim sağlayan çekirdekteki paylaşılan bağlantıdır. Böylece, her indirme için uçtan uca verim şimdi 500 kbps'ye düşürülmüştür.

#### Protokol Katmanları ve Hizmet Modelleri

Şimdiye kadarki tartışmamızdan, internetin son derece karmaşık bir sistem olduğu açıkça görülmektedir. 
İnternetin birçok parçası olduğunu gördük: sayısız **application** ve **protocol**, çeşitli türde **end system**, **packet switch** ve çeşitli türde **link-level media**. Bu muazzam karmaşıklık göz önüne alındığında, bir ağ mimarisini veya en azından ağ mimarisi hakkındaki tartışmamızı organize etmek için herhangi bir umut var mı? Neyse ki, her iki sorunun cevabı da evettir.

#### Katmanlı Mimari (Layered Architecture)

İnternet mimarisi hakkındaki düşüncelerimizi organize etmeye çalışmadan önce, insani bir benzetme arayalım. 
Aslında, günlük hayatımızda sürekli olarak karmaşık sistemlerle uğraşıyoruz. 
Örneğin, birisi sizden havayolu sistemini tanımlamanızı isteseydi, hayal edin. 
Bilet satış görevlileri, bagaj kontrol görevlileri, kapı personeli, pilotlar, uçaklar, hava trafik kontrolü ve uçakları yönlendirmek için dünya çapında bir sistemi olan bu karmaşık sistemi tanımlamak için yapıyı nasıl bulurdunuz? 
Bu sistemi tanımlamanın bir yolu, bir havayoluyla uçarken attığınız (veya başkalarının sizin için attığı) bir dizi eylemi anlatmak olabilir. 
Biletinizi satın alırsınız, bagajınızı kontrol ettirirsiniz, kapıya gidersiniz ve sonunda uçağa binersiniz. Uçak kalkar ve hedefine yönlendirilir. 
Uçağınız indikten sonra, kapıda uçaktan inersiniz ve bagajınızı alırsınız. 
Yolculuk kötü geçtiyse, uçuş hakkında bilet satış görevlisine şikayette bulunursunuz (çabanız için hiçbir şey almadan). 
Şimdiden burada bilgisayar ağı ile bazı benzerlikler görebiliyoruz: Havayolu tarafından kaynaktan hedefe taşınıyorsunuz; bir paket internette kaynak ana bilgisayardan hedef ana bilgisayara gönderilir. Ancak aradığımız tam olarak bu benzetme değil. Örneğin bir benzetme, iki uçta da bir biletleme işlevi olduğunu görüyoruz; ayrıca zaten bileti olan yolcular için bir bagaj işlevi ve zaten bileti olan ve bagajı kontrol edilmiş yolcular için bir kapı işlevi de var. 
Kapıdan geçmiş yolcular için (yani, zaten bileti olan, bagajı kontrol edilmiş ve kapıdan geçmiş yolcular), bir kalkış ve iniş işlevi vardır ve uçuş sırasında bir uçak yönlendirme işlevi vardır. Her katmanın, altındaki katmanlarla birlikte bir işlevsellik, bir hizmet uyguladığına dikkat edin. 
Biletleme katmanında ve altında, bir kişinin havayolu gişesinden diğer havayolu gişesine transferi gerçekleştirilir. 
Bagaj katmanında ve altında, bir kişinin ve bagajının bagaj kontrolünden bagaj teslimine transferi gerçekleştirilir. 
Bagaj katmanının bu hizmeti yalnızca zaten bileti olan bir kişiye sağladığına dikkat edin. Kapı katmanında, bir kişinin ve bagajının kalkış kapısından varış kapısına transferi gerçekleştirilir. Kalkış/iniş katmanında, insanların ve bagajlarının pistten piste transferi gerçekleştirilir. Her katman, (1) o katman içinde belirli eylemleri gerçekleştirerek (örneğin, kapı katmanında, insanları bir uçağa yükleme ve indirme) ve (2) doğrudan altındaki katmanın hizmetlerini kullanarak (örneğin, kapı katmanında, kalkış/iniş katmanının pistten piste yolcu transfer hizmetini kullanarak) hizmetini sağlar.

Katmanlı bir mimari, büyük ve karmaşık bir sistemin iyi tanımlanmış, belirli bir bölümünü tartışmamıza olanak tanır. 
Bu basitleştirme, modülerlik sağlayarak ve katmanın sağladığı hizmetin uygulamasını değiştirmeyi çok daha kolay hale getirerek önemli bir değere sahiptir. 
Katman üstündeki katmana aynı hizmeti sağladığı ve altındaki katmandan aynı hizmetleri kullandığı sürece, bir katmanın uygulaması değiştirildiğinde sistemin geri kalanı değişmeden kalır. (Unutmayın ki, bir hizmetin uygulamasını değiştirmek, hizmetin kendisini değiştirmekten çok farklıdır!) 
Örneğin, kapı işlevleri değiştirilirse (örneğin, insanların boylarına göre uçağa binmesi ve inmesi sağlanırsa), havayolu sisteminin geri kalanı değişmeden kalacaktır çünkü kapı katmanı hala aynı işlevi (insanları yükleme ve indirme) sağlamaktadır; sadece bu işlevi değişiklikten sonra farklı bir şekilde uygulamaktadır. Sürekli güncellenen büyük ve karmaşık sistemler için, bir hizmetin uygulamasını sistemin diğer bileşenlerini etkilemeden değiştirebilme yeteneği, katmanlamanın bir diğer önemli avantajıdır.

#### Protokol Katmanlaması (Protocol Layering)

Havayolları konusunu bir kenara bırakalım ve şimdi ağ protokollerine odaklanalım. 
Ağ protokollerinin tasarımına bir yapı kazandırmak için, ağ tasarımcıları protokolleri—ve bu protokolleri uygulayan ağ donanımını ve yazılımını—katmanlar halinde düzenlerler. Tıpkı havayolu mimarisindeki her işlevin bir katmana ait olması gibi, her protokol de katmanlardan birine aittir.
Yine, bir katmanın üstündeki katmana sunduğu hizmetlerle—bir katmanın sözde **hizmet modeli (service model)**—ilgileniyoruz. 
Havayolu örneğimizde olduğu gibi, her katman hizmetini şu şekilde sağlar: (1) o katman içinde belirli eylemleri gerçekleştirerek ve (2) doğrudan altındaki katmanın hizmetlerini kullanarak.

Örneğin, katman n tarafından sağlanan hizmetler, mesajların ağın bir ucundan diğer ucuna güvenilir bir şekilde teslim edilmesini içerebilir. 
Bu, katman n - 1'in güvenilir olmayan uçtan uca mesaj teslim hizmeti kullanılarak ve kaybolan mesajları tespit edip yeniden iletmek için katman n işlevselliği eklenerek gerçekleştirilebilir.

Bir protokol katmanı **yazılımda (software)**, **donanımda (hardware)** veya ikisinin birleşimiyle uygulanabilir. 
**Uygulama katmanı protokolleri (application-layer protocols)**—örneğin HTTP ve SMTP—neredeyse her zaman uç sistemlerde yazılımda uygulanır. Aynı şekilde **taşıma katmanı protokolleri (transport-layer protocols)** de.

**Fiziksel katman (physical layer)** ve **veri bağlantı katmanı (data link layer)** belirli bir bağlantı üzerinden iletişimi yönetmekle sorumludur. 
Bu nedenle, genellikle belirli bir bağlantıyla ilişkili bir **ağ arabirim kartında (network interface card)** (örneğin, Ethernet veya WiFi arabirim kartları) uygulanırlar. **Ağ katmanı (network layer)** ise sıklıkla donanım ve yazılımın birlikte kullanıldığı bir uygulamadır.

Ayrıca, tıpkı katmanlı havayolu sistemindeki farklı görevlerin (biletleme, bagaj kontrolü, uçuş kontrolü vb.) sistemi oluşturan çeşitli yerlere (havaalanları, kontrol merkezleri gibi) dağıtılması gibi, bir katman n protokolü de ağı oluşturan farklı cihazlara ve sistemlere yayılmıştır.

Yani, genellikle bir katman n protokolünün bir parçası, ağdaki uç sistemlerde (bilgisayarlar, telefonlar gibi), paket anahtarlarında (yönlendiriciler, anahtarlar gibi) ve diğer ağ bileşenlerinde bulunur. Örneğin, internet protokolünün (IP) bir kısmı bilgisayarlarımızda çalışırken, bir kısmı da internet trafiğini yönlendiren yönlendiricilerde aktif olarak görev yapar.

**Protokol katmanlaması (Protocol layering)**, sistemleri anlamak ve yönetmek için bize kavramsal ve yapısal kolaylıklar sağlar [RFC 3439]. 
Gördüğümüz gibi, katmanlama sayesinde karmaşık bir sistemi farklı parçalar halinde inceleyebiliriz. 
**Modülerlik (Modularity)** özelliği sayesinde, sistemin bir bölümünü değiştirmek veya güncellemek gerektiğinde diğer bölümlerden bağımsız hareket edebiliriz. 
Bu da sistemin genelini etkilemeden iyileştirmeler yapmayı kolaylaştırır.

Ancak, bazı araştırmacılar ve ağ uzmanları katmanlama fikrine tamamen katılmamaktadır [Wakeman 1992]. 
Katmanlamanın olası bir dezavantajı, bir katmanın alt katmanların yaptığı işi tekrar edebilmesidir. 
Örneğin, birçok protokol yığını hem bağlantı düzeyinde (örneğin, bir kablo üzerindeki hataları düzeltme) hem de uçtan uca düzeyde (kaynaktan hedefe veri teslimini sağlama) hata kurtarma mekanizmalarına sahip olabilir. Bu da gereksiz bir karmaşıklığa yol açabilir.

İkinci bir potansiyel dezavantaj ise, bir katmandaki bir işlevin çalışması için başka bir katmanda bulunan bilgilere (örneğin, bir zaman damgası değeri) ihtiyaç duyabilmesidir. Bu durum, katmanların birbirinden bağımsız olma prensibine aykırıdır ve bazen verimsizliğe neden olabilir.

Farklı katmanlardaki protokollerin tümüne birlikte **protokol yığını (protocol stack)** adı verilir. 
**İnternet protokol yığını (Internet protocol stack)**, beş temel katmandan oluşur: **fiziksel (physical)**, **bağlantı (link)**, **ağ (network)**, **taşıma (transport)** ve **uygulama (application)** katmanları.

#### Uygulama Katmanı (Application Layer)

Uygulama katmanı, ağ uygulamalarının ve onların protokollerinin bulunduğu yerdir. 
İnternetin uygulama katmanı, HTTP protokolü (Web belgesi isteme ve aktarma için), SMTP (e-posta mesajlarının aktarılması için) ve FTP (iki uç sistem arasında dosya aktarımı için) gibi birçok protokol içerir.

Ayrıca, github.com gibi internet uç sistemleri için insan dostu isimlerin 32 bitlik ağ adresine çevrilmesi gibi bazı ağ işlevlerinin de belirli bir uygulama katmanı protokolü olan **alan adı sistemi (DNS - domain name system)** yardımıyla yapıldığını göreceğiz. 

Bir uygulama katmanı protokolü, birden fazla uç sisteme yayılmıştır. Bir uç sistemdeki uygulama, protokolü kullanarak diğer uç sistemdeki uygulama ile bilgi paketleri alışverişinde bulunur. Uygulama katmanındaki bu bilgi paketine **mesaj (message)** diyeceğiz.

#### Taşıma Katmanı (Transport Layer)

İnternetin taşıma katmanı, uygulama katmanı mesajlarını uygulama uç noktaları arasında taşır. 
İnternette, uygulama katmanı mesajlarını taşıyabilen iki taşıma protokolü bulunur: TCP ve UDP.

TCP, uygulamalarına bağlantı odaklı bir hizmet sunar. Bu hizmet, uygulama katmanı mesajlarının hedefe garantili olarak teslim edilmesini ve akış kontrolünü (yani, gönderici/alıcı hız eşleşmesi) içerir. TCP ayrıca uzun mesajları daha kısa parçalara (segmentlere) böler ve ağ sıkışık olduğunda kaynağın iletim hızını yavaşlatmasını sağlayan bir tıkanıklık kontrol mekanizması sunar.

UDP protokolü ise uygulamalarına bağlantısız bir hizmet sunar. Bu, güvenilirlik, akış kontrolü ve tıkanıklık kontrolü sağlamayan, temel bir hizmettir.
(bir taşıma katmanı paketine **segment** diyeceğiz.)

#### Ağ Katmanı (Network Layer)

İnternetin ağ katmanı, **datagram (datagram)** olarak bilinen ağ katmanı paketlerini bir ana bilgisayardan diğerine taşımaktan sorumludur. 
Kaynak ana bilgisayardaki İnternet taşıma katmanı protokolü (TCP veya UDP), bir taşıma katmanı segmentini ve bir hedef adresi ağ katmanına iletir; tıpkı sizin posta servisine bir hedef adres içeren bir mektup vermeniz gibi. Ağ katmanı daha sonra segmenti hedef ana bilgisayardaki taşıma katmanına teslim etme hizmetini sağlar.

İnternetin ağ katmanı, datagramdaki alanları ve uç sistemlerin ve yönlendiricilerin bu alanlar üzerinde nasıl hareket ettiğini tanımlayan ünlü **IP protokolünü (IP protocol)** içerir. Yalnızca bir IP protokolü vardır ve bir ağ katmanına sahip tüm İnternet bileşenleri IP protokolünü çalıştırmalıdır.

İnternetin ağ katmanı ayrıca datagramların kaynaklar ve hedefler arasında izleyeceği yolları belirleyen **yönlendirme protokollerini (routing protocols)** içerir. İnternet'te birçok yönlendirme protokolü bulunur. Daha önce gördüğümüz gibi, İnternet bir ağlar ağıdır ve bir ağ içinde, ağ yöneticisi istediği herhangi bir yönlendirme protokolünü çalıştırabilir. Ağ katmanı hem IP protokolünü hem de çok sayıda yönlendirme protokolünü içerse de, genellikle basitçe **IP katmanı (IP layer)** olarak adlandırılır ve bu da IP'nin İnternet'i birbirine bağlayan temel unsur olduğunu yansıtır.

#### Bağlantı Katmanı (Link Layer)

İnternetin ağ katmanı, bir datagramı kaynak ile hedef arasındaki bir dizi yönlendirici üzerinden yönlendirir. 
Bir paketi rotadaki bir düğümden (ana bilgisayar veya yönlendirici) bir sonraki düğüme taşımak için, ağ katmanı, bağlantı katmanının hizmetlerine güvenir. Özellikle, her düğümde ağ katmanı datagramı bağlantı katmanına indirir ve bağlantı katmanı datagramı rota üzerindeki bir sonraki düğüme teslim eder. Bu sonraki düğümde, bağlantı katmanı datagramı ağ katmanına geri yukarı iletir.

Bağlantı katmanı tarafından sağlanan hizmetler, bağlantı üzerinde kullanılan belirli **bağlantı katmanı protokolüne (link-layer protocol)** bağlıdır. 
Örneğin, bazı bağlantı katmanı protokolleri, bir bağlantı üzerinden, gönderen düğümden alıcı düğüme güvenilir teslimat sağlar. 
Bu güvenilir teslimat hizmetinin, bir uç sistemden diğerine güvenilir teslimat sağlayan TCP'nin güvenilir teslimat hizmetinden farklı olduğuna dikkat edin.

Bağlantı katmanı protokollerine örnek olarak Ethernet, WiFi ve kablo erişim ağının DOCSIS protokolü verilebilir. 
Datagramların kaynaktan hedefe gitmek için tipik olarak birkaç bağlantıdan geçmesi gerektiğinden, bir datagram rotası boyunca farklı bağlantılarda farklı bağlantı katmanı protokolleri tarafından işlenebilir. Örneğin, bir datagram bir bağlantıda Ethernet tarafından, bir sonraki bağlantıda ise PPP(Noktadan Noktaya İletişim Protokolü) tarafından işlenebilir. Ağ katmanı, farklı bağlantı katmanı protokollerinden farklı hizmetler alacaktır. 
(bağlantı katmanı paketlerine **frame (çerçeve)** diyeceğiz.)

#### Fiziksel Katman (Physical Layer)

Bağlantı katmanının görevi tüm framleri bir ağ elemanından bitişik bir ağ elemanına taşımak iken, fiziksel katmanın görevi frame içindeki tek tek bitleri bir düğümden diğerine taşımaktır. Bu katmandaki protokoller de bağlantıya bağımlıdır ve ayrıca bağlantının gerçek **iletim ortamına (transmission medium)** (örneğin, bükümlü çift bakır tel, tek modlu fiber optik) bağlıdır.

Örneğin, Ethernet'in birçok **fiziksel katman protokolü (physical-layer protocols)** vardır: bükümlü çift bakır tel için bir tane, koaksiyel kablo için başka bir tane, fiber için bir tane ve benzeri. Her durumda, bir bit bağlantı üzerinden farklı bir şekilde taşınır.
