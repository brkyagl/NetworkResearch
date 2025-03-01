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
