# Uygulama Katmanı Giriş

Ağ uygulamaları, bir bilgisayar ağının varlık nedenidir—eğer herhangi bir faydalı uygulama tasavvur edemeseydik, onları destekleyecek bir ağ altyapısına ve protokollerine ihtiyaç olmazdı. İnternetin başlangıcından bu yana, gerçekten de sayısız faydalı ve eğlenceli uygulama yaratılmıştır. 
Bu uygulamalar, internetin başarısının itici gücü olmuş, evlerdeki, okullardaki, hükümetlerdeki ve işletmelerdeki insanları interneti günlük faaliyetlerinin ayrılmaz bir parçası haline getirmeye motive etmiştir.

İnternet uygulamaları, 1970'lerde ve 1980'lerde popüler hale gelen klasik metin tabanlı uygulamaları içerir: metin e-posta (**text e-mail**), bilgisayarlara uzaktan erişim (**remote access**), dosya transferleri (**file transfers**) ve haber grupları (**newsgroups**). 
Bunlara, 1990'ların ortalarının temel uygulaması olan ve web'de gezinme (**Web surfing**), arama (**search**) ve elektronik ticaret (**electronic commerce**) içeren Dünya Çapında Ağ (**World Wide Web**) da dahildir. Yeni milenyumun başından bu yana, Skype, Facetime ve Google Hangouts gibi IP üzerinden ses (**voice over IP**) ve video konferans (**video conferencing**); YouTube gibi kullanıcı tarafından oluşturulan video (**user generated video**) ve Netflix gibi isteğe bağlı filmler (**movies on demand**); Second Life ve World of Warcraft gibi çok oyunculu çevrimiçi oyunlar (**multiplayer online games**) dahil olmak üzere yeni ve oldukça ilgi çekici uygulamalar ortaya çıkmaya devam ediyor.

Aynı dönemde, Facebook, Instagram ve Twitter gibi yeni nesil sosyal ağ uygulamalarının (**social networking applications**) ortaya çıktığını gördük. 
Bu uygulamalar, internetin ağının veya yönlendiricilerinin ve iletişim bağlantılarının üzerinde insan ağları oluşturmuştur. 
Ve en yakın zamanda, akıllı telefonun gelişi ve 4G/5G kablosuz internet erişiminin yaygınlaşmasıyla birlikte, popüler check-in, arkadaşlık ve yol trafik tahmini uygulamaları (Yelp, Tinder ve Waze gibi), mobil ödeme uygulamaları (**mobile payment apps**) (WeChat ve Apple Pay gibi) ve mesajlaşma uygulamaları (**messaging apps**) (WeChat ve WhatsApp gibi) dahil olmak üzere konum tabanlı mobil uygulamalarda (**location based mobile apps**) bir artış yaşanmıştır. 
Açıkça görülüyor ki, yeni ve heyecan verici internet uygulamalarının geliştirilmesinde herhangi bir yavaşlama olmamıştır. 

Bu bölümde, ağ uygulamalarının kavramsal ve uygulama yönlerini inceleyeceğiz. 
Uygulamaların ihtiyaç duyduğu ağ servisleri (**network services**), istemciler (**clients**) ve sunucular (**servers**), süreçler (**processes**) ve taşıma katmanı arayüzleri (**transport-layer interfaces**) dahil olmak üzere temel uygulama katmanı kavramlarını tanımlayarak başlayacağız. 
Web, e-posta (**e-mail**), DNS, eşler arası (P2P) dosya dağıtımı (**peer-to-peer (P2P) file distribution**) ve video akışı (**video streaming**) dahil olmak üzere çeşitli ağ uygulamalarını ayrıntılı olarak inceleyeceğiz. Ardından, hem TCP hem de UDP üzerinden ağ uygulama geliştirmeyi ele alacağız. 
Özellikle, **socket interface (soket arayüzü)**'ni inceleyecek ve Python'da bazı basit istemci-sunucu uygulamalarını adım adım inceleyeceğiz. 

Uygulama katmanı, protokoller (**protocols**) çalışmamıza başlamak için özellikle iyi bir yerdir. Burası tanıdık bir alandır. 
Çalışacağımız protokollere dayanan birçok uygulamayı biliyoruz. Bu bize protokollerin ne hakkında olduğu konusunda iyi bir fikir verecek ve taşıma (**transport**), ağ (**network**) ve bağlantı katmanı protokollerini (**link layer protocols**) incelediğimizde tekrar göreceğimiz birçok aynı sorunla bizi tanıştıracaktır.

## Ağ Uygulamalarının Temelleri

Yeni bir ağ uygulaması fikriniz olduğunu varsayalım. Belki bu uygulama insanlığa büyük bir hizmet sunacak, ya da profesörünüzü memnun edecek, ya da size büyük bir servet getirecek, ya da sadece geliştirmesi eğlenceli olacaktır. Motivasyonunuz ne olursa olsun, şimdi bu fikri gerçek dünya bir ağ uygulamasına nasıl dönüştüreceğinizi inceleyelim.

Ağ uygulama geliştirmenin temelinde, farklı uç sistemlerde çalışan ve ağ üzerinden birbirleriyle iletişim kuran programlar yazmak yatar. 
Örneğin, Web uygulamasında birbirleriyle iletişim kuran iki ayrı program vardır: kullanıcının ana bilgisayarında (masaüstü, dizüstü, tablet, akıllı telefon vb.) çalışan tarayıcı programı (**browser program**); ve Web sunucusu ana bilgisayarında çalışan Web sunucusu programı (**Web server program**). 
Başka bir örnek olarak, Netflix gibi bir İsteğe Bağlı Video (**Video on Demand**) uygulamasında, kullanıcının akıllı telefonunda, tabletinde veya bilgisayarında çalışan Netflix tarafından sağlanan bir program; ve Netflix sunucu ana bilgisayarında çalışan bir Netflix sunucu programı (**Netflix server program**) bulunur. Sunucular (**servers**) genellikle (ancak kesinlikle her zaman değil) bir veri merkezinde (**data center**) barındırılır.

Bu nedenle, yeni uygulamanızı geliştirirken, birden fazla uç sistemde çalışacak yazılım (**software**) yazmanız gerekir. 
Bu yazılım, örneğin C, Java veya Python ile yazılabilir. Önemli olarak, yönlendiriciler (**routers**) veya bağlantı katmanı anahtarları (**link-layer switches**) gibi ağ çekirdek cihazlarında (**network-core devices**) çalışan yazılım yazmanız gerekmez. 
Bu ağ çekirdek cihazları için uygulama yazılımı (**application software**) yazmak isteseniz bile bunu yapamazsınız. 
Ağ çekirdek cihazları uygulama katmanında (**application layer**) değil, bunun yerine daha alt katmanlarda—özellikle ağ katmanında (**network layer**) ve altında işlev görür. Uygulama yazılımını uç sistemlerle (**end systems**) sınırlayan bu temel tasarım, çok çeşitli ağ uygulamalarının hızlı bir şekilde geliştirilmesini ve kullanıma sunulmasını kolaylaştırmıştır.

### Ağ Uygulama Mimarileri

Yazılım kodlamasına dalmadan önce, uygulamanız için geniş bir mimari plana sahip olmalısınız. 
Unutmayın ki bir uygulamanın mimarisi, ağ mimarisinden belirgin şekilde farklıdır. Uygulama geliştiricisinin bakış açısıyla, ağ mimarisi sabittir ve uygulamalara belirli bir hizmet kümesi sağlar. Uygulama mimarisi ise uygulama geliştiricisi tarafından tasarlanır ve uygulamanın çeşitli uç sistemler üzerinde nasıl yapılandırılacağını belirler. Uygulama mimarisini seçerken, bir uygulama geliştiricisi muhtemelen modern ağ uygulamalarında kullanılan iki baskın mimari paradigmadan birine başvuracaktır: istemci-sunucu mimarisi (**client-server architecture**) veya eşler arası (P2P) mimarisi (**peer-to-peer (P2P) architecture**).

İstemci-sunucu mimarisinde, sunucu (**server**) adı verilen her zaman açık bir ana bilgisayar bulunur ve bu ana bilgisayar, istemci (**clients**) adı verilen birçok diğer ana bilgisayardan gelen istekleri karşılar. Klasik bir örnek, istemci ana bilgisayarlarında çalışan tarayıcılardan istekleri karşılayan her zaman açık bir Web sunucusunun (**Web server**) bulunduğu Web uygulamasıdır (**Web application**). 
Bir Web sunucusu, bir istemci ana bilgisayarından bir nesne için bir istek aldığında, istenen nesneyi istemci ana bilgisayarına göndererek yanıt verir. 
İstemci-sunucu mimarisinde, istemcilerin doğrudan birbirleriyle iletişim kurmadığını unutmayın; örneğin, Web uygulamasında iki tarayıcı doğrudan iletişim kurmaz. İstemci-sunucu mimarisinin bir diğer özelliği de sunucunun IP adresi (**IP address**) adı verilen sabit, iyi bilinen bir adrese sahip olmasıdır. 
Sunucu sabit, iyi bilinen bir adrese sahip olduğu ve sunucu her zaman açık olduğu için, bir istemci sunucunun IP adresine bir paket göndererek sunucuyla her zaman iletişim kurabilir. İstemci-sunucu mimarisine sahip daha iyi bilinen uygulamalardan bazıları Web, FTP, Telnet ve e-posta'dır (**e-mail**). 

Çoğu zaman bir istemci-sunucu uygulamasında, tek bir sunucu ana bilgisayarı istemcilerden gelen tüm isteklere yetişemez. 
Örneğin, popüler bir sosyal ağ sitesi (**social-networking site**) tüm isteklerini işleyen yalnızca bir sunucuya sahipse hızla aşırı yüklenebilir. 
Bu nedenle, çok sayıda ana bilgisayarı barındıran bir veri merkezi (**data center**), güçlü bir sanal sunucu (**virtual server**) oluşturmak için sıklıkla kullanılır. Arama motorları (**search engines**) (örneğin Google, Bing, Baidu), internet ticareti (**Internet commerce**) (örneğin Amazon, eBay, Alibaba), web tabanlı e-posta (**Web-based e-mail**) (örneğin Gmail ve Yahoo Mail), sosyal medya (**social media**) (örneğin Facebook, Instagram, Twitter ve WeChat) gibi en popüler internet servisleri bir veya daha fazla veri merkezinde çalışır. Google'ın dünya çapında dağılmış en az 19+ veri merkezi bulunmaktadır ve bunlar toplu olarak arama, YouTube, Gmail ve diğer hizmetleri yönetir. Bir veri merkezi yüz binlerce sunucuya sahip olabilir ve bunların güçlendirilmesi ve bakımı gerekir.
Ek olarak, servis sağlayıcılar veri merkezlerinden veri göndermek için tekrar eden bağlantı ve bant genişliği maliyetlerini karşılamalıdır.

P2P mimarisinde, veri merkezlerindeki özel sunuculara minimum (veya hiç) bağımlılık vardır. 
Bunun yerine uygulama, eşler (**peers**) adı verilen aralıklı olarak bağlanan ana bilgisayar çiftleri arasındaki doğrudan iletişimi kullanır. 
Eşler, servis sağlayıcısına ait değildir, bunun yerine çoğu evlerde, üniversitelerde ve ofislerde bulunan kullanıcılar tarafından kontrol edilen masaüstü ve dizüstü bilgisayarlardır. Eşler özel bir sunucu üzerinden geçmeden iletişim kurdukları için, mimariye eşler arası denir. 
Popüler bir P2P uygulamasına bir örnek, dosya paylaşım uygulaması BitTorrent'tir. P2P mimarilerinin en çekici özelliklerinden biri, kendi kendine ölçeklenebilirliğidir (**self-scalability**). Örneğin, bir P2P dosya paylaşım uygulamasında, her eş dosya isteyerek iş yükü oluştursa da, her eş aynı zamanda dosyaları diğer eşlere dağıtarak sisteme hizmet kapasitesi de ekler. P2P mimarileri aynı zamanda maliyet etkilidir, çünkü normalde önemli bir sunucu altyapısı ve sunucu bant genişliği gerektirmezler (veri merkezlerine sahip istemci-sunucu tasarımlarının aksine). 
Ancak, P2P uygulamaları yüksek derecede merkezi olmayan yapıları nedeniyle güvenlik, performans ve güvenilirlik sorunlarıyla karşı karşıyadır.

### İletişim Kuran Süreçler

Ağ uygulamanızı oluşturmadan önce, birden fazla uç sistemde çalışan programların birbirleriyle nasıl iletişim kurduğuna dair temel bir anlayışa da ihtiyacınız vardır. İşletim sistemleri jargonunda, aslında iletişim kuran programlar değil, süreçlerdir (**processes**).

Bir süreç (**process**), bir uç sistem (**end system**) içinde çalışan bir program (**program**) olarak düşünülebilir. 
Süreçler aynı uç sistem üzerinde çalışırken, uç sistemin işletim sistemi (**operating system**) tarafından yönetilen kuralları kullanarak süreçler arası iletişim (**interprocess communication**) ile birbirleriyle iletişim kurabilirler.

İki farklı uç sistemdeki süreçler, bilgisayar ağı (**computer network**) üzerinden mesajlar (**messages**) alışverişi yaparak birbirleriyle iletişim kurarlar. 
Bir gönderen süreç (**sending process**) mesajlar oluşturur ve bunları ağa gönderir; bir alıcı süreç (**receiving process**) bu mesajları alır ve muhtemelen mesajlar geri göndererek yanıt verir.

### İstemci ve Sunucu Süreçleri

Bir ağ uygulaması, bir ağ üzerinden birbirlerine mesaj gönderen süreç çiftlerinden oluşur. 
Örneğin, Web uygulamasında bir istemci tarayıcı süreci (**client browser process**) bir Web sunucu süreci (**Web server process**) ile mesaj alışverişinde bulunur. Bir P2P dosya paylaşım sisteminde (**P2P file-sharing system**), bir eşteki (**peer**) bir süreçten başka bir eşteki bir sürece bir dosya aktarılır. 
İletişim kuran her süreç çifti için, tipik olarak iki süreçten birini istemci (**client**) ve diğer süreci sunucu (**server**) olarak etiketleriz. 
Web'de, bir tarayıcı bir istemci süreci ve bir Web sunucusu bir sunucu sürecidir. P2P dosya paylaşımında (**P2P file sharing**), dosyayı indiren eş istemci olarak, dosyayı yükleyen eş ise sunucu olarak etiketlenir.

P2P dosya paylaşımı gibi bazı uygulamalarda, bir sürecin hem istemci hem de sunucu olabileceğini gözlemlemiş olabilirsiniz. 
Gerçekten de, bir P2P dosya paylaşım sistemindeki bir süreç hem dosya yükleyebilir hem de dosya indirebilir. 
Yine de, iki süreç arasındaki herhangi bir iletişim oturumu bağlamında, bir süreci istemci ve diğer süreci sunucu olarak etiketleyebiliriz. 

İstemci ve sunucu süreçlerini aşağıdaki gibi tanımlıyoruz:

İki süreç arasındaki bir iletişim oturumu bağlamında, iletişimi başlatan (yani oturumun başında diğer süreçle ilk iletişimi kuran) süreç istemci olarak etiketlenir. Oturumu başlatmak için iletişim kurulmasını bekleyen süreç ise sunucudur.

Web'de, bir tarayıcı süreci bir Web sunucu süreciyle iletişimi başlatır; bu nedenle tarayıcı süreci istemci ve Web sunucu süreci sunucudur. 
P2P dosya paylaşımında, Eş A (**Peer A**) Eş B'den (**Peer B**) belirli bir dosyayı göndermesini istediğinde, bu özel iletişim oturumu bağlamında Eş A istemci ve Eş B sunucudur.

Karışıklık olmadığında, bazen "bir uygulamanın istemci tarafı ve sunucu tarafı" terminolojisini de kullanacağız. 

### Süreç ve Bilgisayar Ağı Arasındaki Arayüz

Yukarıda belirtildiği gibi, çoğu uygulama, her bir çifte ait iki sürecin birbirlerine mesaj gönderdiği iletişim kuran süreç çiftlerinden oluşur. 
Bir süreçten diğerine gönderilen herhangi bir mesaj, alttaki ağdan geçmelidir. Bir süreç, bir yazılım arayüzü olan soket (**socket**) aracılığıyla ağa mesaj gönderir ve ağdan mesaj alır. Süreçleri ve soketleri anlamamıza yardımcı olacak bir benzetme düşünelim. Bir süreç bir eve benzetilebilir ve onun soketi de kapısına benzetilebilir. Bir süreç başka bir ana bilgisayardaki (**host**) başka bir sürece bir mesaj göndermek istediğinde, mesajı kapısından (soketinden) dışarı iter. 
Bu gönderen süreç, kapısının diğer tarafında mesajı hedef sürecin kapısına taşıyacak bir ulaşım altyapısının (**transportation infrastructure**) olduğunu varsayar. Mesaj hedef ana bilgisayara ulaştığında, mesaj alıcı sürecin kapısından (soketinden) geçer ve alıcı süreç daha sonra mesaj üzerine işlem yapar.

İnternet üzerinden iletişim kuran iki süreç arasındaki soket iletişimi olsun, (süreçler tarafından kullanılan temel taşıma protokolünün (**transport protocol**) internetin TCP protokolü olduğunu varsayalım.) Bu senaryoda, bir soket, bir ana bilgisayar içindeki uygulama katmanı (**application layer**) ve taşıma katmanı (**transport layer**) arasındaki arayüzdür. Aynı zamanda, soket ağ uygulamalarının oluşturulduğu programlama arayüzü olduğu için, uygulama (**application**) ve ağ (**network**) arasındaki Uygulama Programlama Arayüzü (API) (**Application Programming Interface (API)**) olarak da adlandırılır. 
Uygulama geliştiricisi (**application developer**), soketin uygulama katmanı tarafındaki her şey üzerinde kontrole sahiptir, ancak soketin taşıma katmanı tarafında çok az kontrole sahiptir. Uygulama geliştiricisinin taşıma katmanı tarafındaki tek kontrolü (1) taşıma protokolünün seçimi ve (2) belki de maksimum arabellek (**maximum buffer**) ve maksimum segment boyutları (**maximum segment sizes**) gibi birkaç taşıma katmanı parametresini sabitleme yeteneğidir. 
Uygulama geliştiricisi bir taşıma protokolü seçtikten sonra (bir seçim mevcutsa), uygulama bu protokol tarafından sağlanan taşıma katmanı hizmetleri kullanılarak oluşturulur. 

### Süreçlerin Adreslenmesi

Belirli bir hedefe posta göndermek için, hedefin bir adresi olması gerekir. 
Benzer şekilde, bir ana bilgisayarda çalışan bir sürecin başka bir ana bilgisayarda çalışan bir sürece paket (**packets**) gönderebilmesi için, alıcı sürecin (**receiving process**) bir adresi olması gerekir. Alıcı süreci tanımlamak için iki bilgi parçasının belirtilmesi gerekir: (1) ana bilgisayarın adresi (**host**) ve (2) hedef ana bilgisayardaki (**destination host**) alıcı süreci belirten bir tanımlayıcı.

İnternette, ana bilgisayar IP adresi (**IP address**) ile tanımlanır. Şimdilik bilmemiz gereken tek şey, bir IP adresinin ana bilgisayarı benzersiz bir şekilde tanımladığını düşünebileceğimiz 32 bitlik bir miktar olduğudur. Bir mesajın (**message**) gideceği ana bilgisayarın adresini bilmenin yanı sıra, gönderen sürecin ayrıca ana bilgisayarda çalışan alıcı süreci (daha doğrusu, alıcı soketi) tanımlaması gerekir. Bu bilgiye ihtiyaç duyulur çünkü genel olarak bir ana bilgisayar birçok ağ uygulaması çalıştırıyor olabilir. Bir hedef port numarası (**destination port number**) bu amaca hizmet eder. 
Popüler uygulamalara belirli port numaraları atanmıştır. Örneğin, bir Web sunucusu (**Web server**) 80 numaralı port ile tanımlanır. 
Bir posta sunucu süreci (SMTP protokolünü kullanarak) 25 numaralı port ile tanımlanır. Tüm İnternet standart protokolleri için iyi bilinen port numaralarının (**well-known port numbers**) bir listesi www.iana.org adresinde bulunabilir. 

