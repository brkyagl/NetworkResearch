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
