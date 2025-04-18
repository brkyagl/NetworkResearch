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

### Uygulamalara Sunulan Taşıma Hizmetleri

Bir soketin, uygulama süreci ile taşıma katmanı protokolü arasındaki arayüz olduğunu hatırlayın. 
Gönderen taraftaki uygulama, mesajları soket üzerinden iter. Soketin diğer tarafında, taşıma katmanı protokolü, mesajları alıcı sürecin soketine ulaştırma sorumluluğuna sahiptir.

İnternet dahil birçok ağ, birden fazla taşıma katmanı protokolü sunar. Bir uygulama geliştirirken, mevcut taşıma katmanı protokollerinden birini seçmelisiniz. 
Bu seçimi nasıl yaparsınız? Büyük olasılıkla, mevcut taşıma katmanı protokolleri tarafından sağlanan hizmetleri inceler ve ardından uygulamanızın ihtiyaçlarına en uygun hizmetlere sahip olan protokolü seçersiniz. 
Bu durum, iki şehir arasında seyahat etmek için tren veya uçak ulaşımını seçmeye benzer. Birini veya diğerini seçmek zorundasınız ve her ulaşım şekli farklı hizmetler sunar. (Örneğin, tren şehir merkezinden alım ve bırakma sunarken, uçak daha kısa seyahat süresi sunar.)

Bir taşıma katmanı protokolünün, onu çağıran uygulamalara sunabileceği hizmetler nelerdir? Olası hizmetleri dört ana boyutta sınıflandırabiliriz: güvenilir veri transferi (**reliable data transfer**), verim (**throughput**), zamanlama (**timing**) ve güvenlik (**security**).

#### Güvenilir Veri Transferi

Paketler bir bilgisayar ağı içinde kaybolabilir. Örneğin, bir paket bir yönlendiricideki (**router**) bir arabelleği (**buffer**) aşabilir veya bazı bitleri bozulduktan sonra bir ana bilgisayar (**host**) veya yönlendirici tarafından atılabilir. Elektronik posta (**electronic mail**), dosya transferi (**file transfer**), uzak ana bilgisayar erişimi (**remote host access**), Web belgesi transferleri (**Web document transfers**) ve finansal uygulamalar (**financial applications**) gibi birçok uygulama için veri kaybı yıkıcı sonuçlara yol açabilir (ikincisi durumda, banka veya müşteri için!). 
Bu nedenle, bu uygulamaları desteklemek için, uygulamanın bir ucundan gönderilen verilerin uygulamanın diğer ucuna doğru ve eksiksiz olarak teslim edilmesini garanti etmek için bir şeyler yapılması gerekir. 
Bir protokol böyle garantili bir veri teslim hizmeti sağlıyorsa, güvenilir veri transferi (**reliable data transfer**) sağladığı söylenir. 
Bir taşıma katmanı protokolünün (**transport-layer protocol**) bir uygulamaya potansiyel olarak sağlayabileceği önemli bir hizmet, süreçten sürece güvenilir veri transferidir (**process-to-process reliable data transfer**). Bir taşıma protokolü bu hizmeti sağladığında, gönderen süreç (**sending process**) verilerini sokete (**socket**) iletebilir ve verilerin alıcı sürece (**receiving process**) hatasız olarak ulaşacağından tamamen emin olabilir.

Bir taşıma katmanı protokolü güvenilir veri transferi sağlamadığında, gönderen süreç tarafından gönderilen verilerin bir kısmı asla alıcı sürece ulaşmayabilir. 
Bu durum, veri kaybına toleranslı uygulamalar (**loss-tolerant applications**), özellikle de bir miktar veri kaybını tolere edebilen konuşma amaçlı ses/video (**conversational audio/video**) gibi multimedya uygulamaları (**multimedia applications**) için kabul edilebilir olabilir. Bu multimedya uygulamalarında, kaybolan veriler ses/videoda küçük bir aksaklığa neden olabilir—kritik bir bozulma değildir.

#### Verim (Throughput)

Bir ağ yolu üzerindeki iki süreç arasındaki bir iletişim oturumu bağlamında, gönderen sürecin alıcı sürece bitleri iletebileceği hız olan kullanılabilir verim (**available throughput**) kavramını tanıtmıştık. 
Ağ yolu üzerindeki bant genişliğini (**bandwidth**) başka oturumlar da paylaştığı ve bu diğer oturumlar gelip gideceği için, kullanılabilir verim zamanla dalgalanabilir. 
Bu gözlemler, bir taşıma katmanı protokolünün sağlayabileceği başka doğal bir hizmete, yani belirli bir oranda garantili kullanılabilir verime (**guaranteed available throughput**) yol açar. 
Böyle bir hizmetle, uygulama saniyede r bit (**bits/sec**) garantili bir verim talep edebilir ve taşıma protokolü daha sonra kullanılabilir verimin her zaman en az saniyede r bit olmasını sağlar. 
Böyle bir garantili verim hizmeti birçok uygulamaya cazip gelecektir. Örneğin, bir İnternet telefon uygulaması sesi 32 kbps hızında kodluyorsa, bu hızda ağa veri göndermesi ve verilerin alıcı uygulamaya teslim edilmesi gerekir. Taşıma protokolü bu verimi sağlayamazsa, uygulama daha düşük bir hızda kodlama yapmak (ve bu düşük kodlama hızını sürdürmek için yeterli verimi almak) zorunda kalabilir veya vazgeçmek zorunda kalabilir, çünkü örneğin, gereken verimin yarısını almak bu İnternet telefon uygulaması için çok az veya hiç işe yaramaz. Verim gereksinimleri olan uygulamalara bant genişliğine duyarlı uygulamalar (**bandwidth-sensitive applications**) denir. Mevcut birçok multimedya uygulaması bant genişliğine duyarlıdır, ancak bazı multimedya uygulamaları, o anda mevcut olan verime uyan bir oranda sayısallaştırılmış sesi veya videoyu kodlamak için uyarlanabilir kodlama teknikleri (**adaptive coding techniques**) kullanabilir.

Bant genişliğine duyarlı uygulamaların belirli verim gereksinimleri varken, esnek uygulamalar (**elastic applications**) mevcut olan verimi istedikleri kadar kullanabilirler. 
Elektronik posta (**Electronic mail**), dosya transferi (**file transfer**) ve Web transferleri (**Web transfers**) hepsi esnek uygulamalardır. 
Elbette, verim ne kadar yüksek olursa o kadar iyidir. Çok zengin, çok zayıf veya çok fazla verime sahip olunamayacağını söyleyen bir atasözü vardır!

#### Zamanlama (Timing)

Bir taşıma katmanı protokolü, zamanlama garantileri de sağlayabilir. Verim garantilerinde olduğu gibi, zamanlama garantileri de birçok şekil ve biçimde olabilir. 
Bir örnek garanti, göndericinin sokete pompaladığı her bitin, alıcının soketine en fazla 100 milisaniye (**msec**) sonra ulaşması olabilir. 
Böyle bir hizmet, İnternet telefon görüşmeleri (**Internet telephony**), sanal ortamlar (**virtual environments**), telekonferans (**teleconferencing**) ve çok oyunculu oyunlar (**multiplayer games**) gibi etkileşimli gerçek zamanlı uygulamalar (**interactive real-time applications**) için cazip olacaktır. Bu uygulamaların tümü, etkili olabilmek için veri teslimatında sıkı zamanlama kısıtlamaları (**timing constraints**) gerektirir, bkz. [Gauthier 1999; Ramjee 1994]. Örneğin, İnternet telefon görüşmelerindeki uzun gecikmeler, konuşmada doğal olmayan duraklamalara neden olma eğilimindedir; çok oyunculu bir oyunda veya sanal etkileşimli ortamda, bir eylemde bulunmak ile ortamdan (örneğin, uçtan uca bir bağlantının (**end-to-end connection**) sonundaki başka bir oyuncudan) yanıtı görmek arasındaki uzun bir gecikme, uygulamanın daha az gerçekçi hissettirmesine neden olur. Gerçek zamanlı olmayan uygulamalar (**non-real-time applications**) için daha düşük gecikme her zaman daha yüksek gecikmeye tercih edilir, ancak uçtan uca gecikmeler üzerinde sıkı bir kısıtlama yoktur.

#### Güvenlik (Security)

Son olarak, bir taşıma protokolü bir uygulamaya bir veya daha fazla güvenlik hizmeti sunabilir. Örneğin, gönderen ana bilgisayarda (**sending host**) bir taşıma protokolü, gönderen süreç (**sending process**) tarafından iletilen tüm verileri şifreleyebilir (**encrypt**) ve alıcı ana bilgisayarda (**receiving host**), taşıma katmanı protokolü (**transport-layer protocol**) verileri alıcı sürece (**receiving process**) teslim etmeden önce şifresini çözebilir (**decrypt**). Böyle bir hizmet, veriler gönderen ve alan süreçler arasında bir şekilde gözlemlense bile, iki süreç arasında gizlilik (**confidentiality**) sağlayacaktır. 
Bir taşıma protokolü, gizliliğe ek olarak veri bütünlüğü (**data integrity**) ve uç nokta kimlik doğrulaması (**end-point authentication**) dahil olmak üzere başka güvenlik hizmetleri de sağlayabilir.

### İnternet Tarafından Sağlanan Taşıma Hizmetleri

Bu noktaya kadar, genel olarak bir bilgisayar ağının sağlayabileceği taşıma hizmetlerini ele alıyorduk. Şimdi daha spesifik olalım ve İnternet tarafından sağlanan taşıma hizmetlerinin türünü inceleyelim. 
İnternet (ve daha genel olarak TCP/IP ağları), uygulamalara UDP ve TCP olmak üzere iki taşıma protokolü sunar. Siz (bir uygulama geliştiricisi olarak) İnternet için yeni bir ağ uygulaması oluşturduğunuzda, vermeniz gereken ilk kararlardan biri UDP mi yoksa TCP mi kullanacağınızdır. Bu protokollerin her biri, çağıran uygulamalara farklı bir hizmet kümesi sunar. 

Seçilmiş bazı uygulamaların hizmet gereksinimleri:

```

| Uygulama                  | Veri Kaybı    | Verim                                     | Zamana Duyarlı |
|---------------------------|---------------|-------------------------------------------|----------------|
| Dosya transferi/indirme   | Kayıpsız      | Esnek                                     | Hayır          |
| E-posta                   | Kayıpsız      | Esnek                                     | Hayır          |
| Web belgeleri             | Kayıpsız      | Esnek (birkaç kbps)                       | Hayır          |
| İnternet telefon görüşmesi| Kayıp toleranslı | Ses: birkaç kbps–1 Mbps Video: 10 kbps–5 Mbps | Evet: 100'lerce ms |
| Kayıtlı ses/video akışı   | Kayıp toleranslı | Yukarıdakiyle aynı                        | Evet: birkaç saniye |
| Etkileşimli oyunlar       | Kayıp toleranslı | Birkaç kbps–10 kbps                       | Evet: 100'lerce ms |
| Akıllı telefon mesajlaşma | Kayıpsız      | Esnek                                     | Evet ve hayır |
```

#### TCP Hizmetleri

TCP hizmet modeli, bağlantı odaklı bir hizmet (**connection-oriented service**) ve güvenilir veri transferi hizmetini (**reliable data transfer service**) içerir. 
Bir uygulama, taşıma protokolü olarak TCP'yi çağırdığında, uygulama TCP'den bu iki hizmeti de alır.

* **Bağlantı odaklı hizmet.** TCP, uygulama katmanı mesajları akmaya başlamadan önce istemcinin ve sunucunun birbirleriyle taşıma katmanı kontrol bilgilerini alışverişi yapmasını sağlar.
Bu sözde el sıkışma prosedürü (**handshaking procedure**), istemciyi ve sunucuyu uyararak, bir paket (**packets**) saldırısına hazırlanmalarına olanak tanır. El sıkışma aşamasından sonra, iki sürecin soketleri (**sockets**) arasında bir TCP bağlantısının (**TCP connection**) var olduğu söylenir. Bağlantı, iki sürecin aynı anda bağlantı üzerinden birbirlerine mesaj gönderebileceği tam çift yönlü (**full-duplex connection**) bir bağlantıdır. Uygulama mesaj göndermeyi bitirdiğinde, bağlantıyı sonlandırması gerekir. 

* **Güvenilir veri transferi hizmeti.** İletişim kuran süreçler (**communicating processes**), gönderilen tüm verilerin hatasız ve doğru sırada teslim edilmesi için TCP'ye güvenebilirler.
Uygulamanın bir tarafı bir sokete bir bayt akışı (**stream of bytes**) ilettiğinde, TCP'nin aynı bayt akışını kayıp veya yinelenen bayt olmaksızın alıcı sokete (**receiving socket**) teslim edeceğine güvenebilir.

TCP ayrıca, iletişim kuran süreçlerin doğrudan yararından ziyade İnternetin genel refahı için bir hizmet olan bir tıkanıklık kontrol mekanizması (**congestion-control mechanism**) içerir. 
TCP tıkanıklık kontrol mekanizması, gönderen ve alıcı arasındaki ağ sıkıştığında bir gönderen süreci (istemci veya sunucu) yavaşlatır. TCP tıkanıklık kontrolü ayrıca her TCP bağlantısını ağ bant genişliğinin adil payıyla sınırlamaya çalışır.

#### UDP Hizmetleri

UDP, minimum hizmet sağlayan, gösterişsiz, hafif bir taşıma protokolüdür (**transport protocol**). UDP bağlantısızdır (**connectionless**), bu nedenle iki süreç iletişim kurmaya başlamadan önce herhangi bir el sıkışma (**handshaking**) olmaz. UDP, güvenilmez bir veri transferi hizmeti (**unreliable data transfer service**) sağlar—yani, bir süreç bir UDP soketine (**UDP socket**) bir mesaj gönderdiğinde, UDP mesajın alıcı sürece (**receiving process**) ulaşıp ulaşmayacağına dair hiçbir garanti vermez. Dahası, alıcı sürece ulaşan mesajlar sırasız olarak ulaşabilir.

#### TCP'Yİ GÜVENLİ HALE GETİRME

Ne TCP ne de UDP herhangi bir şifreleme (**encryption**) sağlamaz—gönderen sürecin soketine ilettiği veri, ağ üzerinden hedef sürece giden aynı veridir. 
Bu nedenle, örneğin, gönderen süreç soketine açık metin (**cleartext**) olarak (yani, şifrelenmemiş) bir parola (**password**) gönderirse, açık metin parola gönderen ve alıcı arasındaki tüm bağlantılar (**links**) üzerinden geçer ve potansiyel olarak herhangi bir ara bağlantıda dinlenebilir ve keşfedilebilir. Gizlilik ve diğer güvenlik sorunları birçok uygulama için kritik hale geldiğinden, İnternet topluluğu TCP için Taşıma Katmanı Güvenliği (TLS) (**Transport Layer Security (TLS)**) [RFC 5246] adı verilen bir geliştirme geliştirmiştir. TLS ile geliştirilmiş TCP (**TCP-enhanced-with-TLS**), geleneksel TCP'nin yaptığı her şeyi yapmakla kalmaz, aynı zamanda şifreleme, veri bütünlüğü (**data integrity**) ve uç nokta kimlik doğrulaması (**end-point authentication**) dahil olmak üzere kritik süreçten sürece güvenlik hizmetleri (**process-to-process security services**) sağlar. TLS'nin TCP ve UDP ile aynı düzeyde üçüncü bir İnternet taşıma protokolü (**Internet transport protocol**) olmadığını, bunun yerine geliştirmelerin uygulama katmanında (**application layer**) uygulandığı bir TCP geliştirmesi olduğunu vurguluyoruz. Özellikle, bir uygulama TLS hizmetlerini kullanmak istiyorsa, uygulamanın hem istemci (**client**) hem de sunucu (**server**) taraflarına TLS kodu (mevcut, yüksek düzeyde optimize edilmiş kütüphaneler ve sınıflar) eklemesi gerekir. TLS'nin geleneksel TCP soket API'sine benzer kendi soket API'si (**TLS socket API**) vardır. 
Bir uygulama TLS kullandığında, gönderen süreç TLS soketine açık metin verisi iletir; gönderen ana bilgisayardaki TLS daha sonra verileri şifreler ve şifrelenmiş verileri TCP soketine iletir. 
Şifrelenmiş veri, İnternet üzerinden alıcı süreçteki TCP soketine gider. Alıcı soket, şifrelenmiş veriyi şifresini çözen TLS'ye iletir. Son olarak, TLS açık metin verisini TLS soketi aracılığıyla alıcı sürece iletir. 

---- 

UDP bir tıkanıklık kontrol mekanizması içermez, bu nedenle UDP'nin gönderen tarafı aşağıdaki katmana (ağ katmanı) istediği hızda veri pompalayabilir. (Ancak, aradaki bağlantıların sınırlı iletim kapasitesi veya tıkanıklık nedeniyle gerçek uçtan uca verimin bu orandan daha düşük olabileceğini unutmayın).

### İnternet Taşıma Protokolleri Tarafından Sağlanmayan Hizmetler

Bu noktaya kadar, taşıma protokolü hizmetlerini dört boyutta düzenledik: güvenilir veri transferi, verim, zamanlama ve güvenlik. Bu hizmetlerden hangileri TCP ve UDP tarafından sağlanmaktadır? TCP'nin güvenilir uçtan uca veri transferi sağladığını zaten belirtmiştik. Ayrıca TCP'nin güvenlik hizmetleri sağlamak için TLS ile uygulama katmanında kolayca geliştirilebileceğini de biliyoruz. Ancak TCP ve UDP'nin kısa açıklamamızda, verim veya zamanlama garantilerinden—bugünün İnternet taşıma protokolleri tarafından sağlanmayan hizmetlerden—gözle görülür bir şekilde bahsedilmemiştir. 
Bu, İnternet telefon görüşmeleri gibi zamana duyarlı uygulamaların bugünün İnternet'inde çalışamayacağı anlamına mı geliyor? Cevap açıkça hayır—İnternet yıllardır zamana duyarlı uygulamalara ev sahipliği yapmaktadır. Bu uygulamalar genellikle oldukça iyi çalışır çünkü bu garanti eksikliğiyle mümkün olduğunca başa çıkmak için tasarlanmışlardır. Yine de, gecikme aşırı olduğunda veya uçtan uca verim sınırlı olduğunda akıllı tasarımın sınırları vardır. Özetle, günümüz İnterneti genellikle zamana duyarlı uygulamalara tatmin edici hizmet sağlayabilir, ancak herhangi bir zamanlama veya verim garantisi sağlayamaz.

Bazı popüler İnternet uygulamaları tarafından kullanılan taşıma protokollerini göstermektedir. E-posta, uzak terminal erişimi, Web ve dosya transferinin tümü TCP'yi kullanmaktadır. 
Bu uygulamalar öncelikle TCP'yi seçmiştir çünkü TCP, tüm verilerin sonunda hedefine ulaşacağını garanti eden güvenilir veri transferi sağlar. Skype gibi İnternet telefon görüşmesi uygulamaları genellikle bir miktar kaybı tolere edebilse de, etkili olabilmek için minimum bir hıza ihtiyaç duyduklarından, İnternet telefon uygulamalarının geliştiricileri genellikle uygulamalarını UDP üzerinden çalıştırmayı tercih ederler, böylece TCP'nin tıkanıklık kontrol mekanizmasını ve paket yüklerini atlatırlar. Ancak birçok güvenlik duvarı (çoğu UDP trafiği türünü) engelleyecek şekilde yapılandırıldığından, İnternet telefon uygulamaları genellikle UDP iletişimi başarısız olursa yedek olarak TCP'yi kullanacak şekilde tasarlanır.

```
| Uygulama Katmanı Protokolü   | Uygulama Katmanı Protokolü   | Temel Taşıma Protokolü 
|------------------------------------|----------------------- |
| Elektronik posta               (SMTP [RFC 5321])            |  TCP
| Uzak terminal erişimi          (Telnet [RFC 854])           |  TCP              
| Web                            (HTTP 1.1 [RFC 7230])        |  TCP                   
| Dosya transferi                (FTP [RFC 959])              |  TCP             
| Akışkan multimedya             (HTTP (örn., YouTube), DASH) |  TCP                   
| İnternet telefon görüşmesi     (SIP [RFC 3261], RTP [RFC 3550] veya özel (örn., Skype)) | UDP veya TCP     
```

### Uygulama Katmanı Protokolleri

Az önce, ağ süreçlerinin soketlere mesaj göndererek birbirleriyle iletişim kurduğunu öğrendik. Peki bu mesajlar nasıl yapılandırılıyor? 
Mesajlardaki çeşitli alanların anlamları nelerdir? Süreçler ne zaman mesaj gönderir? Bu sorular bizi uygulama katmanı protokolleri (**application-layer protocols**) alanına götürür. 
Bir uygulama katmanı protokolü, farklı uç sistemlerde (**end systems**) çalışan bir uygulamanın süreçlerinin (**application’s processes**) birbirlerine nasıl mesaj ilettiğini tanımlar. 

Özellikle, bir uygulama katmanı protokolü şunları tanımlar:

* Örneğin, istek mesajları (**request messages**) ve yanıt mesajları (**response messages**) gibi değiş tokuş edilen mesaj türleri.
* Mesajdaki alanlar ve alanların nasıl sınırlandırıldığı gibi çeşitli mesaj türlerinin sözdizimi (**syntax**).
* Alanların semantiği (**semantics**), yani alanlardaki bilginin anlamı.
* Bir sürecin ne zaman ve nasıl mesaj gönderdiğini ve mesajlara nasıl yanıt verdiğini belirleyen kurallar.

Bazı uygulama katmanı protokolleri RFC'lerde belirtilmiştir ve bu nedenle kamu malıdır (**public domain**). Örneğin, Web'in uygulama katmanı protokolü olan HTTP (Köprü Metni Transfer Protokolü (**HyperText Transfer Protocol**) [RFC 7230]), bir RFC olarak mevcuttur. Bir tarayıcı geliştiricisi (**browser developer**) HTTP RFC'sinin kurallarına uyarsa, tarayıcı da HTTP RFC'sinin kurallarına uymuş olan herhangi bir Web sunucusundan (**Web server**) Web sayfalarını (**Web pages**) alabilecektir. Diğer birçok uygulama katmanı protokolü tescillidir (**proprietary**) ve kasıtlı olarak kamu malı değildir. Örneğin, Skype tescilli uygulama katmanı protokolleri kullanır.

Ağ uygulamaları (**network applications**) ve uygulama katmanı protokolleri arasında ayrım yapmak önemlidir. Bir uygulama katmanı protokolü, bir ağ uygulamasının yalnızca bir parçasıdır (her ne kadar bizim açımızdan uygulamanın çok önemli bir parçası olsa da!). Birkaç örneğe bakalım. Web, kullanıcıların istedikleri zaman Web sunucularından belge almalarını sağlayan bir istemci-sunucu uygulamasıdır (**client-server application**). Web uygulaması, belge formatları için bir standart (yani, HTML), Web tarayıcıları (**Web browsers**) (örneğin, Chrome ve Microsoft Internet Explorer), Web sunucuları (**Web servers**) (örneğin, Apache ve Microsoft sunucuları) ve bir uygulama katmanı protokolü dahil olmak üzere birçok bileşenden oluşur. Web'in uygulama katmanı protokolü olan HTTP, tarayıcı ve Web sunucusu arasında değiş tokuş edilen mesajların formatını ve sırasını tanımlar. Bu nedenle HTTP, Web uygulamasının yalnızca bir parçasıdır (her ne kadar önemli bir parça olsa da). Başka bir örnek olarak, Netflix'in video hizmetinin de birçok bileşeni olduğunu göreceğiz: video depolayan ve ileten sunucular (**servers**), faturalandırmayı ve diğer istemci işlevlerini yöneten diğer sunucular, istemciler (örneğin, akıllı telefonunuzdaki, tabletinizdeki veya bilgisayarınızdaki Netflix uygulaması) ve bir uygulama katmanı DASH protokolü (**DASH protocol**), bir Netflix sunucusu (**Netflix server**) ve istemcisi arasında değiş tokuş edilen mesajların formatını ve sırasını tanımlar. Bu nedenle DASH, Netflix uygulamasının yalnızca bir parçasıdır (her ne kadar önemli bir parça olsa da).

## Web ve HTTP

1990'ların başlarına kadar, internet öncelikle araştırmacılar, akademisyenler ve üniversite öğrencileri tarafından uzak ana bilgisayarlara oturum açmak, yerel ana bilgisayarlardan uzak ana bilgisayarlara dosya aktarmak ve tam tersi, haber almak ve göndermek, ve elektronik posta alıp göndermek için kullanılıyordu. Bu uygulamalar son derece kullanışlı olsa da (ve olmaya devam etse de), internet akademik ve araştırma çevrelerinin dışında esasen bilinmiyordu. Ardından, 1990'ların başlarında, sahneye büyük yeni bir uygulama çıktı—Dünya Çapında Ağ (**World Wide Web**) [Berners-Lee 1994]. 
Web, genel halkın dikkatini çeken ilk internet uygulamasıydı. İnsanların iş ortamlarında ve dışında nasıl etkileşimde bulunduklarını önemli ölçüde değiştirdi. 
İnterneti birçok veri ağı arasından esasen tek veri ağı konumuna yükseltti.

Belki de kullanıcıları en çok çeken şey, Web'in isteğe bağlı çalışmasıdır. Kullanıcılar istedikleri şeyi, istedikleri zaman alırlar. 
Bu, içerik sağlayıcının içeriği yayınladığı zaman kullanıcının ona uymasını zorlayan geleneksel yayın radyosu (**broadcast radio**) ve televizyonun (**television**) aksinedir. 
İsteğe bağlı olarak kullanılabilir olmasının yanı sıra, Web'in insanların sevdiği ve değer verdiği birçok harika özelliği daha vardır. 
Herhangi bir bireyin Web üzerinden bilgi sunması son derece kolaydır—herkes çok düşük maliyetle yayıncı olabilir. Köprü bağlantılar (**Hyperlinks**) ve arama motorları (**search engines**), bilgi okyanusunda gezinmemize yardımcı olur. Fotoğraflar (**Photos**) ve videolar (**videos**), duyularımızı harekete geçirir. Formlar (**Forms**), JavaScript, video ve diğer birçok araç, sayfalarla ve sitelerle etkileşim kurmamızı sağlar. Web ve protokolleri, YouTube, Web tabanlı e-posta (**Web-based e-mail**) (Gmail gibi) ve Instagram ile Google Haritalar dahil olmak üzere çoğu mobil internet uygulaması için bir platform görevi görür.

### HTTP'ye Genel Bakış

Web'in uygulama katmanı protokolü (**application-layer protocol**) olan Köprü Metni Transfer Protokolü (HTTP) (**HyperText Transfer Protocol (HTTP)**), Web'in kalbinde yer alır. [RFC 1945], [RFC 7230] ve [RFC 7540]'ta tanımlanmıştır. HTTP, iki programda uygulanır: bir istemci programı (**client program**) ve bir sunucu programı (**server program**). 
Farklı uç sistemlerde (**end systems**) çalışan istemci programı ve sunucu programı, HTTP mesajları (**HTTP messages**) alışverişi yaparak birbirleriyle konuşur. 
HTTP, bu mesajların yapısını ve istemci ile sunucunun mesajları nasıl değiş tokuş edeceğini tanımlar. HTTP'yi ayrıntılı olarak açıklamadan önce, bazı Web terminolojilerini gözden geçirmeliyiz.

Bir Web sayfası (**Web page**) (aynı zamanda belge de denir) nesnelerden (**objects**) oluşur. 
Bir nesne, basitçe bir HTML dosyası (**HTML file**), bir JPEG görüntüsü (**JPEG image**), bir Javascript dosyası (**Javascrpt file**), bir CSS stil sayfası dosyası (**CCS style sheet file**) veya bir video klibi (**video clip**) gibi tek bir URL ile adreslenebilen bir dosyadır. Çoğu Web sayfası bir temel HTML dosyası (**base HTML file**) ve birkaç referans verilen nesneden (**referenced objects**) oluşur. 
Örneğin, bir Web sayfası HTML metni ve beş JPEG görüntüsü içeriyorsa, Web sayfasının altı nesnesi vardır: temel HTML dosyası + beş görüntü. 
Temel HTML dosyası, sayfadaki diğer nesneleri nesnelerin URL'leri (**URLs**) ile referans alır. Her URL'nin iki bileşeni vardır: nesneyi barındıran sunucunun ana bilgisayar adı (**hostname**) ve nesnenin yol adı (**path name**). Örneğin, `http://www.github.com/RedBerks/picture.jpg` URL'sinin ana bilgisayar adı **www.github.com** ve yol adı **/RedBerks/picture.jpg**'dir. 
Web tarayıcıları (**Web browsers**) (Internet Explorer ve Chrome gibi) HTTP'nin istemci tarafını (**client side**) uyguladığından, Web bağlamında tarayıcı ve istemci (**client**) kelimelerini birbirinin yerine kullanacağız. HTTP'nin sunucu tarafını (**server side**) uygulayan Web sunucuları (**Web servers**), her biri bir URL ile adreslenebilen Web nesnelerini barındırır. Popüler Web sunucuları arasında Apache ve Microsoft Internet Information Server bulunur.

HTTP, Web istemcilerinin (**HTTP clients**) Web sunucularından Web sayfalarını nasıl istediğini ve sunucuların Web sayfalarını istemcilere nasıl aktardığını tanımlar. 
İstemci ve sunucu arasındaki etkileşimi daha sonra ayrıntılı olarak tartışacağız. Bir kullanıcı bir Web sayfası istediğinde (örneğin, bir hyperlinke tıklar), tarayıcı sayfadaki nesneler için sunucuya HTTP istek mesajları (**HTTP request messages**) gönderir. Sunucu istekleri alır ve nesneleri içeren HTTP yanıt mesajları (**HTTP response messages**) ile yanıt verir.

HTTP, altında yatan taşıma protokolü olarak TCP'yi (**TCP**) kullanır (UDP üzerinde çalışmak yerine). HTTP istemcisi önce sunucuyla bir TCP bağlantısı (**TCP connection**) başlatır. 
Bağlantı kurulduktan sonra, tarayıcı ve sunucu süreçleri soket arayüzleri (**socket interfaces**) aracılığıyla TCP'ye erişir. İstemci tarafında soket arayüzü, istemci süreci (**client process**) ve TCP bağlantısı arasındaki kapıdır (**door**); sunucu tarafında ise sunucu süreci (**server process**) ve TCP bağlantısı arasındaki kapıdır. 
İstemci, soket arayüzüne HTTP istek mesajları gönderir ve soket arayüzünden HTTP yanıt mesajları alır. Benzer şekilde, HTTP sunucusu soket arayüzünden istek mesajları alır ve soket arayüzüne yanıt mesajları gönderir. Bir istemci soket arayüzüne bir mesaj gönderdiğinde, mesaj istemcinin elinden çıkar ve TCP'nin "eline" geçer. TCP HTTP'ye güvenilir bir veri transferi hizmeti (**reliable data transfer service**) sağlar. Bu, bir istemci süreci tarafından gönderilen her HTTP istek mesajının sonunda sunucuya bozulmadan (**intact**) ulaşacağı anlamına gelir; benzer şekilde, sunucu süreci tarafından gönderilen her HTTP yanıt mesajı da sonunda istemciye bozulmadan ulaşır. Burada katmanlı mimarinin (**layered architecture**) büyük avantajlarından birini görüyoruz—HTTP'nin kaybolan veriler veya TCP'nin ağ içindeki veri kaybını veya yeniden sıralanmasını nasıl kurtardığının ayrıntıları hakkında endişelenmesine gerek yoktur. Bu, TCP'nin ve protokol yığınının (**protocol stack**) alt katmanlarındaki protokollerin işidir.

Sunucunun, istemci hakkında herhangi bir durum bilgisi (**state information**) saklamadan istenen dosyaları istemcilere gönderdiğini belirtmek önemlidir.
Belirli bir istemci birkaç saniye içinde aynı nesneyi iki kez isterse, sunucu nesneyi az önce istemciye sunduğunu söyleyerek yanıt vermez; bunun yerine, daha önce ne yaptığını tamamen unutmuş olduğu için nesneyi yeniden gönderir. Bir HTTP sunucusu istemciler hakkında hiçbir bilgi saklamadığı için, HTTP **stateless protocol (durumsuz protokol)** olarak adlandırılır. 
Ayrıca, istemci-sunucu uygulama mimarisini (**client-server application architecture**) kullandığını da belirtmek gerekir. Bir Web sunucusu her zaman açıktır, sabit bir IP adresine sahiptir ve potansiyel olarak milyonlarca farklı tarayıcıdan gelen isteklere hizmet verir.

HTTP'nin orijinal versiyonu HTTP/1.0 olarak adlandırılır ve 1990'ların başlarına dayanır [RFC 1945]. HTTP işlemlerinin çoğu HTTP/1.1 üzerinden gerçekleşmektedir [RFC 7230]. 
Ancak, giderek artan sayıda tarayıcı ve Web sunucusu, HTTP/2 [RFC 7540] adı verilen yeni bir HTTP sürümünü de desteklemektedir. 

### Kalıcı Olmayan ve Kalıcı Bağlantılar

Birçok İnternet uygulamasında, istemci ve sunucu uzun bir süre iletişim kurar, istemci bir dizi istekte bulunur ve sunucu her bir isteğe yanıt verir.
Uygulamaya ve uygulamanın nasıl kullanıldığına bağlı olarak, istek dizisi art arda, düzenli aralıklarla periyodik olarak veya aralıklı olarak yapılabilir. 
Bu istemci-sunucu etkileşimi TCP üzerinden gerçekleşirken, uygulama geliştiricisinin önemli bir karar vermesi gerekir—her istek/yanıt çifti ayrı bir TCP bağlantısı (**TCP connection**) üzerinden mi gönderilmeli, yoksa tüm istekler ve bunlara karşılık gelen yanıtlar aynı TCP bağlantısı üzerinden mi gönderilmelidir? İlk yaklaşımda, uygulamanın kalıcı olmayan bağlantılar (**non-persistent connections**) kullandığı söylenir; ikinci yaklaşımda ise kalıcı bağlantılar (**persistent connections**). Bu tasarım sorununu derinlemesine anlamak için, kalıcı bağlantıların avantajlarını ve dezavantajlarını, hem kalıcı olmayan hem de kalıcı bağlantıları kullanabilen HTTP bağlamında inceleyelim. HTTP, varsayılan modunda kalıcı bağlantılar kullanmasına rağmen, HTTP istemcileri ve sunucuları bunun yerine kalıcı olmayan bağlantıları kullanacak şekilde yapılandırılabilir.

#### Kalıcı Olmayan Bağlantılarla HTTP

Kalıcı olmayan bağlantılar durumunda, bir Web sayfasını sunucudan istemciye aktarma adımlarını inceleyelim. 
Sayfanın bir temel HTML dosyasından ve 10 JPEG görüntüsünden oluştuğunu ve bu 11 nesnenin tamamının aynı sunucuda bulunduğunu varsayalım. 
Ayrıca, temel HTML dosyasının URL'sinin şu olduğunu varsayalım: `http://www.redberks.com/home.index`

İşte olanlar:

1. HTTP istemci süreci, HTTP için varsayılan port numarası olan 80 numaralı portta `www.redberks.com` sunucusuna bir TCP bağlantısı başlatır.
TCP bağlantısıyla ilişkili olarak, istemcide bir soket ve sunucuda bir soket olacaktır.

2. HTTP istemcisi, soketi aracılığıyla sunucuya bir HTTP istek mesajı (**HTTP request message**) gönderir. İstek mesajı `/home.index` yol adını (**path name**) içerir. 

3. HTTP sunucu süreci, soketi aracılığıyla istek mesajını alır, depolama alanından (RAM veya disk) `/home.index` nesnesini alır, nesneyi bir HTTP yanıt mesajına (**HTTP response message**) kapsüller ve yanıt mesajını soketi aracılığıyla istemciye gönderir.

4. HTTP sunucu süreci, TCP'ye TCP bağlantısını kapatmasını söyler. (Ancak TCP, istemcinin yanıt mesajını bozulmadan (**intact**) aldığından emin olana kadar bağlantıyı fiilen sonlandırmaz.)

5. HTTP istemcisi yanıt mesajını alır. TCP bağlantısı sonlanır. Mesaj, kapsüllenmiş nesnenin bir HTML dosyası olduğunu belirtir. İstemci, dosyayı yanıt mesajından çıkarır, HTML dosyasını inceler ve 10 JPEG nesnesine referansları bulur.

6. İlk dört adım, referans verilen her bir JPEG nesnesi için tekrarlanır. Tarayıcı Web sayfasını aldıkça, sayfayı kullanıcıya görüntüler. İki farklı tarayıcı, bir Web sayfasını biraz farklı şekillerde yorumlayabilir (yani kullanıcıya görüntüleyebilir). HTTP'nin bir Web sayfasının bir istemci tarafından nasıl yorumlandığıyla hiçbir ilgisi yoktur. HTTP spesifikasyonları ([RFC 1945] ve [RFC 7540]), yalnızca istemci HTTP programı ile sunucu HTTP programı arasındaki iletişim protokolünü tanımlar.

Yukarıdaki adımlar, sunucunun nesneyi gönderdikten sonra her TCP bağlantısının kapatıldığı kalıcı olmayan bağlantıların (**non-persistent connections**) kullanımını göstermektedir—bağlantı diğer nesneler için kalıcı olmaz. HTTP/1.0, kalıcı olmayan TCP bağlantıları kullanır. Her kalıcı olmayan TCP bağlantısının tam olarak bir istek mesajı ve bir yanıt mesajı taşıdığını unutmayın. 
Böylece, bu örnekte, bir kullanıcı Web sayfasını istediğinde 11 TCP bağlantısı oluşturulur.

Yukarıda açıklanan adımlarda, istemcinin 10 JPEG'yi 10 seri TCP bağlantısı üzerinden mi yoksa JPEG'lerin bazılarının paralel TCP bağlantıları (**parallel TCP connections**) üzerinden mi aldığını bilerek muğlak tuttuk. Gerçekten de, kullanıcılar bazı tarayıcıları paralellik derecesini kontrol etmek için yapılandırabilirler. Tarayıcılar birden fazla TCP bağlantısı açabilir ve Web sayfasının farklı kısımlarını birden fazla bağlantı üzerinden isteyebilirler. Bir sonraki bölümde göreceğimiz gibi, paralel bağlantıların (**parallel connections**) kullanılması yanıt süresini (**response time**) kısaltır.

Devam etmeden önce, istemcinin temel HTML dosyasını istediği andan itibaren tüm dosyanın istemci tarafından alınana kadar geçen süreyi tahmin etmek için hızlı bir hesaplama yapalım. 
Bu amaçla, küçük bir paketin istemciden sunucuya ve sonra tekrar istemciye gitmesi için geçen süre olan gidiş-dönüş süresini (RTT) (**round-trip time (RTT)**) tanımlıyoruz. 
RTT, paket yayılma gecikmelerini (**packet-propagation delays**), ara yönlendirici ve anahtarlardaki paket kuyruklama gecikmelerini (**packet-queuing delays**), ve paket işleme gecikmelerini (**packet-processing delays**) içerir. Şimdi bir kullanıcı bir köprü bağlantıya (**hyperlink**) tıkladığında ne olduğunu düşünelim. Bu durum tarayıcının tarayıcı ve Web sunucusu arasında bir TCP bağlantısı başlatmasına neden olur; bu bir "üçlü el sıkışma" (**three-way handshake**) içerir—istemci sunucuya küçük bir TCP segmenti gönderir, sunucu onaylar (**acknowledges**) ve küçük bir TCP segmenti ile yanıt verir, ve son olarak istemci sunucuya geri onaylar (**acknowledgment**). Üçlü el sıkışmanın ilk iki kısmı bir RTT sürer. El sıkışmanın ilk iki kısmını tamamladıktan sonra, istemci HTTP istek mesajını üçlü el sıkışmanın üçüncü kısmı (onay) ile birleştirerek TCP bağlantısına gönderir. İstek mesajı sunucuya ulaştığında, sunucu HTML dosyasını TCP bağlantısına gönderir. Bu HTTP istek/yanıtı bir RTT daha alır. 
Dolayısıyla, kabaca, toplam yanıt süresi iki RTT artı HTML dosyasının sunucudaki iletim süresidir (**transmission time**).

#### Kalıcı Bağlantılarla HTTP

Kalıcı olmayan bağlantıların bazı dezavantajları vardır. İlk olarak, istenen her nesne için yepyeni bir bağlantı kurulmalı ve korunmalıdır. 
Bu bağlantıların her biri için hem istemcide hem de sunucuda TCP arabellekleri (**TCP buffers**) tahsis edilmeli ve TCP değişkenleri (**TCP variables**) tutulmalıdır. Bu durum, aynı anda yüzlerce farklı istemciden gelen isteklere hizmet veren Web sunucusu (**Web server**) üzerinde önemli bir yük oluşturabilir. İkinci olarak, az önce açıkladığımız gibi, her nesne iki RTT (**RTTs**) kadar bir teslimat gecikmesi yaşar—biri TCP bağlantısını kurmak için, diğeri ise nesneyi istemek ve almak için.

HTTP/1.1 kalıcı bağlantılarında (**HTTP/1.1 persistent connections**), sunucu bir yanıt gönderdikten sonra TCP bağlantısını (**TCP connection**) açık bırakır. 
Aynı istemci ve sunucu arasındaki sonraki istekler ve yanıtlar aynı bağlantı üzerinden gönderilebilir. Özellikle, tüm bir Web sayfası (yukarıdaki örnekte, temel HTML dosyası ve 10 görüntü) tek bir kalıcı TCP bağlantısı üzerinden gönderilebilir. Dahası, aynı sunucuda bulunan birden fazla Web sayfası da tek bir kalıcı TCP bağlantısı üzerinden sunucudan aynı istemciye gönderilebilir. 
Bu nesne istekleri, bekleyen yanıtlara yanıt beklemeden art arda yapılabilir (**pipelining**). Tipik olarak, HTTP sunucusu belirli bir süre kullanılmadığında (yapılandırılabilir bir zaman aşımı aralığı (**timeout interval**) sonunda) bağlantıyı kapatır. Sunucu, art arda gelen istekleri aldığında, nesneleri art arda gönderir. HTTP'nin varsayılan modu, pipelining ile kalıcı bağlantıları kullanır. 

#### HTTP Mesaj Formatı

HTTP spesifikasyonları [RFC 1945; RFC 7230; RFC 7540], HTTP mesaj formatlarının (**HTTP message formats**) tanımlarını içerir. 
İki tür HTTP mesajı (**HTTP messages**) vardır: istek mesajları (**request messages**) ve yanıt mesajları (**response messages**). 

