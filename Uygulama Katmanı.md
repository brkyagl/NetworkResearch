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

#### HTTP İstek Mesajı

Aşağıda tipik bir HTTP istek mesajı örneği verilmiştir:

```
GET /home.html HTTP/1.1
Host: www.redberks.com
Connection: close
User-agent: Mozilla/5.0
Accept-language: tr
```

Bu basit istek mesajını yakından inceleyerek birçok şey öğrenebiliriz. Öncelikle, mesajın sıradan ASCII metniyle yazıldığını görüyoruz, böylece sıradan bir bilgisayar okuryazarı tarafından okunabilir. 
İkinci olarak, mesajın beş satırdan oluştuğunu ve her satırın ardından bir satır başı (**carriage return**) ve bir satır besleme (**line feed**) geldiğini görüyoruz. 
Son satırın ardından ek bir satır başı ve satır besleme gelir. Bu özel istek mesajı beş satır olmasına rağmen, bir istek mesajı daha fazla veya en az bir satıra sahip olabilir. 
Bir HTTP istek mesajının ilk satırına istek satırı (**request line**) denir; sonraki satırlar başlık satırlarıdır (**header lines**). 
İstek satırının üç alanı vardır: method alanı (**method field**), URL alanı (**URL field**) ve HTTP versiyon alanı (**HTTP version field**). 
Method alanı, GET, POST, HEAD, PUT ve DELETE dahil olmak üzere birkaç farklı değer alabilir. HTTP istek mesajlarının büyük çoğunluğu GET methodunu kullanır.
GET methodu, tarayıcı istenen nesneyi talep ettiğinde kullanılır ve istenen nesne URL alanında belirtilir. Bu örnekte, tarayıcı `/home.html` nesnesini talep ediyor. Versiyon kendi kendini açıklayıcıdır; bu örnekte tarayıcı HTTP/1.1 versiyonunu kullanmaktadır.

Şimdi örnekteki başlık satırlarına bakalım. `Host: www.redberks.com` başlık satırı, nesnenin bulunduğu ana bilgisayarı belirtir. 
Sunucuya zaten bir TCP bağlantısı kurulmuş olduğundan bu başlık satırının gereksiz olduğunu düşünebilirsiniz. Ancak, host başlık satırı tarafından sağlanan bilgi Web proxy önbellekleri (**Web proxy caches**) tarafından gereklidir. `Connection: close` başlık satırını ekleyerek, tarayıcı sunucuya kalıcı bağlantılarla (**persistent connections**) uğraşmak istemediğini söyler; istenen nesneyi gönderdikten sonra sunucunun bağlantıyı kapatmasını ister. `User-agent:` başlık satırı, kullanıcı ajanını (**User agent**), yani sunucuya istekte bulunan tarayıcı türünü belirtir. 
Burada kullanıcı ajanı Mozilla/5.0, bir Firefox tarayıcısıdır. Bu başlık satırı kullanışlıdır çünkü sunucu, aynı nesnenin farklı versiyonlarını farklı kullanıcı ajanlarına gönderebilir. (Her versiyon aynı URL ile adreslenir.) Son olarak, `Accept-language:` başlığı, sunucuda böyle bir nesne mevcutsa, kullanıcının nesnenin Türkçe versiyonunu almayı tercih ettiğini gösterir; aksi takdirde sunucu varsayılan versiyonunu göndermelidir. `Accept-language:` başlığı, HTTP'de bulunan birçok içerik anlaşması başlığından (**content negotiation headers**) sadece biridir.

Bir örneğe baktıktan sonra, şimdi bir istek mesajının genel formatına bakalım. Genel formatın önceki örneğimize yakından uyduğunu görelim. 
Ancak, başlık satırlarından (ve ek satır başı ve satır beslemeden) sonra bir "varlık gövdesi" (**entity body**) olduğunu bilin. Varlık gövdesi GET methodunda boştur, ancak POST methodunda kullanılır. 
Bir HTTP istemcisi, kullanıcı bir formu doldurduğunda—örneğin, bir kullanıcı bir arama motoruna arama kelimeleri sağladığında—sıklıkla POST methodunu kullanır. 
Bir POST mesajıyla, kullanıcı sunucudan hala bir Web sayfası talep ediyor, ancak Web sayfasının belirli içeriği kullanıcının form alanlarına girdiği şeye bağlıdır. 
Eğer method alanının değeri POST ise, varlık gövdesi kullanıcının form alanlarına girdiği şeyi içerir.

Bir formla oluşturulan bir isteğin mutlaka POST methodunu kullanması gerekmediğini belirtmezsek eksik kalırdık. 
Bunun yerine, HTML formları (**HTML forms**) genellikle GET methodunu kullanır ve girilen veriyi (**inputted data**) (form alanlarındaki) istenen URL'ye dahil eder. 
Örneğin, bir form GET methodunu kullanıyorsa, iki alanı varsa ve iki alana girilenler "Monster" ve "Huawei" ise, URL yapısı `www.redberks.com/computersearch?monster&huawei` şeklinde olacaktır. 
Günlük Web gezintinizde muhtemelen bu tür uzatılmış URL'ler fark etmişsinizdir.

HEAD methodu GET methoduna benzer. Sunucu HEAD methodu ile bir istek aldığında, bir HTTP mesajı ile yanıt verir ancak istenen nesneyi dışarıda bırakır. 
Uygulama geliştiricileri hata ayıklama için genellikle HEAD methodunu kullanır. PUT methodu genellikle Web yayınlama araçlarıyla (**Web publishing tools**) birlikte kullanılır. 
Bir kullanıcının belirli bir Web sunucusunda (**Web server**) belirli bir yola (dizine) bir nesne yüklemesine (**upload**) olanak tanır.
PUT methodu ayrıca nesneleri Web sunucularına yüklemesi gereken uygulamalar tarafından da kullanılır. DELETE methodu, bir kullanıcının veya bir uygulamanın bir Web sunucusundaki bir nesneyi silmesine (**delete**) olanak tanır.

#### HTTP Yanıt Mesajı

Aşağıda tipik bir HTTP yanıt mesajı verilmiştir. Bu yanıt mesajı, az önce tartışılan örnek istek mesajının yanıtı olabilir.

```
HTTP/1.1 200 OK
Connection: close
Date: Tue, 29 Aug 2025 15:44:04 GMT
Server: Apache/2.2.3 (CentOS)
Last-Modified: Tue, 29 Aug 2025 15:11:03 GMT
Content-Length: 6821
Content-Type: text/html
(data data data data data ...)
```

Bu yanıt mesajını dikkatlice inceleyelim. Üç bölümden oluşur: başlangıçta bir durum satırı (**status line**), altı başlık satırı (**header lines**) ve ardından varlık gövdesi (**entity body**). Varlık gövdesi mesajın ana içeriğidir—istenen nesnenin kendisini içerir (data data data data data ... ile temsil edilir). 
Durum satırının üç alanı vardır: protokol versiyon alanı (**protocol version field**), bir durum kodu (**status code**) ve buna karşılık gelen bir durum mesajı (**status message**). Bu örnekte, durum satırı sunucunun HTTP/1.1 kullandığını ve her şeyin OK olduğunu (yani, sunucunun istenen nesneyi bulduğunu ve gönderdiğini) belirtir.

Şimdi başlık satırlarına bakalım. Sunucu, mesajı gönderdikten sonra TCP bağlantısını kapatacağını istemciye bildirmek için `Connection: close` başlık satırını kullanır. `Date:` başlık satırı, HTTP yanıtının sunucu tarafından oluşturulup gönderildiği zamanı ve tarihi belirtir. 
Bunun nesnenin oluşturulduğu veya en son değiştirildiği zaman olmadığını unutmayın; bu, sunucunun nesneyi dosya sisteminden aldığı, nesneyi yanıt mesajına yerleştirdiği ve yanıt mesajını gönderdiği zamandır. `Server:` başlık satırı, mesajın bir Apache Web sunucusu tarafından oluşturulduğunu belirtir; bu, HTTP istek mesajındaki `User-agent:` başlık satırına benzer. `Last-Modified:` başlık satırı, nesnenin oluşturulduğu veya en son değiştirildiği zamanı ve tarihi belirtir. Yakında daha ayrıntılı olarak ele alacağımız `Last-Modified:` başlığı, hem yerel istemcide hem de ağ önbellek sunucularında (**network cache servers**) (proxy sunucuları (**proxy servers**) olarak da bilinir) nesne önbelleğe alma (**object caching**) için kritiktir. `Content-Length:` başlık satırı, gönderilen nesnenin bayt cinsinden boyutunu belirtir. `Content-Type:` başlık satırı, varlık gövdesindeki nesnenin HTML metni olduğunu belirtir. (Nesne türü resmi olarak `Content-Type:` başlığı ile belirtilir, dosya uzantısı ile değil.)

Bir örneğe baktıktan sonra, şimdi bir yanıt mesajının genel formatını inceleyelim. 
Yanıt mesajının bu genel formatı, önceki yanıt mesajı örneğiyle eşleşmektedir. Durum kodları ve bunlarla ilişkili ifadeler hakkında birkaç ek söz söyleyelim. Durum kodu ve ilişkili ifade, isteğin sonucunu gösterir. Bazı yaygın durum kodları (**status codes**) ve ilişkili ifadeler şunlardır:

```
* **200 OK:** İstek başarılı oldu ve bilgi yanıtta döndürüldü.
* **301 Moved Permanently:** İstenen nesne kalıcı olarak taşınmıştır; yeni URL, yanıt mesajının `Location:` başlığında belirtilir. İstemci yazılımı yeni URL'yi otomatik olarak alacaktır.
* **400 Bad Request:** Bu, isteğin sunucu tarafından anlaşılamadığını belirten genel bir hata kodudur.
* **404 Not Found:** İstenen belge bu sunucuda mevcut değildir.
* **505 HTTP Version Not Supported:** İstenen HTTP protokol versiyonu sunucu tarafından desteklenmemektedir.
```

Gerçek bir HTTP yanıt mesajı görmek ister misiniz? Bu şiddetle tavsiye edilir ve yapması çok kolaydır! 
İlk olarak favori Web sunucunuza Telnet (**Telnet**) yapın. Ardından, sunucuda barındırılan bir nesne için tek satırlık bir istek mesajı yazın. 
Örneğin, bir komut istemine (**command prompt**) erişiminiz varsa şunu yazın:

```bash
telnet httpbin.org 80
```

Ardından şunu yazın:

```
GET /forms/post HTTP/1.1
Host: httpbin.org 
```

![resim](https://i.ibb.co/7xDCT9td/Telnet-Http-Req.png)

(Son satırı yazdıktan sonra satır başı tuşuna iki kez basın.) Bu, httpbin.org ana bilgisayarının 80 numaralı portuna bir TCP bağlantısı açar ve ardından HTTP istek mesajını gönderir. Bu temel HTML dosyasını içeren bir yanıt mesajı görmelisiniz(httpbin sitesinin form pathi). 
Sadece HTTP mesaj satırlarını görmek ve nesnenin kendisini almak istemiyorsanız, GET yerine HEAD yazın.

HTTP istek ve yanıt mesajlarında kullanılabilecek bir dizi başlık satırını tartıştık. 
HTTP spesifikasyonu, tarayıcılar, Web sunucuları ve ağ önbellek sunucuları tarafından eklenebilecek çok, çok daha fazla başlık satırı tanımlar. 
Başlık satırlarının toplamının sadece küçük bir kısmını ele aldık. Aşağıda birkaçını daha ve ağ Web önbelleğe almayı tartışırken birkaç küçük sayısını daha ele alacağız. HTTP protokolü, başlıkları ve durum kodları dahil olmak üzere oldukça okunaklı ve kapsamlı bir tartışma [Krishnamurthy 2001]'de verilmiştir.

Bir tarayıcı, bir istek mesajına hangi başlık satırlarını dahil edeceğine nasıl karar verir? Bir Web sunucusu, bir yanıt mesajına hangi başlık satırlarını dahil edeceğine nasıl karar verir? Bir tarayıcı, tarayıcı türü ve sürümü, tarayıcının kullanıcı yapılandırması ve tarayıcının şu anda önbelleğe alınmış (**cached**), ancak muhtemelen güncel olmayan, bir nesne sürümüne sahip olup olmadığına bağlı olarak başlık satırları oluşturacaktır. 
Web sunucuları benzer şekilde davranır: Farklı ürünler (**products**), sürümler (**versions**) ve yapılandırmalar (**configurations**) vardır, bunların hepsi yanıt mesajlarına hangi başlık satırlarının dahil edileceğini etkiler.

#### Kullanıcı-Sunucu Etkileşimi: Çerezler (Cookies)

Yukarıda bir HTTP sunucusunun durumsuz (**stateless**) olduğunu belirtmiştik. 
Bu, sunucu tasarımını basitleştirir ve mühendislerin binlerce eşzamanlı TCP bağlantısını yönetebilen yüksek performanslı Web sunucuları geliştirmesine olanak tanımıştır. Ancak, bir Web sitesinin kullanıcıları tanımlaması genellikle istenir, ya sunucu kullanıcı erişimini kısıtlamak istediği için ya da kullanıcı kimliğine bağlı olarak içerik sunmak istediği için. Bu amaçlarla HTTP çerezleri (**cookies**) kullanır. [RFC 6265]'te tanımlanan çerezler, sitelerin kullanıcıları takip etmesine olanak tanır. Çoğu büyük ticari Web sitesi bugün çerez kullanmaktadır.

Çerez teknolojisinin dört bileşeni vardır: (1) HTTP yanıt mesajında bir çerez başlık satırı (**cookie header line**); (2) HTTP istek mesajında bir çerez başlık satırı; (3) kullanıcının uç sisteminde tutulan ve kullanıcının tarayıcısı (**user’s browser**) tarafından yönetilen bir çerez dosyası (**cookie file**); ve (4) Web sitesinde bir arka uç veritabanı (**back-end database**). Çerezlerin nasıl çalıştığına dair bir örnek üzerinden geçelim. 
Susan'ın, ev bilgisayarından İnternet Explorer kullanarak Web'e her zaman erişen bir kullanıcının, Amazon.com ile ilk kez iletişim kurduğunu varsayalım. 
Diyelim ki daha önce eBay sitesini ziyaret etmiş. İstek Amazon Web sunucusuna (**Amazon Web server**) geldiğinde, sunucu benzersiz bir kimlik numarası (**identification number**) oluşturur ve arka uç veritabanında bu kimlik numarasıyla indekslenmiş bir giriş yaratır. 
Amazon Web sunucusu daha sonra Susan'ın tarayıcısına yanıt verir ve HTTP yanıtına kimlik numarasını içeren bir `Set-cookie:` başlığı ekler. 
Örneğin, başlık satırı şöyle olabilir:

`Set-cookie: 1678891298`

Susan'ın tarayıcısı HTTP yanıt mesajını aldığında, `Set-cookie:` başlığını görür. 
Tarayıcı daha sonra yönettiği özel çerez dosyasına bir satır ekler. Bu satır, sunucunun ana bilgisayar adını ve `Set-cookie:` başlığındaki kimlik numarasını içerir. Susan'ın daha önce eBay sitesini ziyaret ettiği için çerez dosyasında eBay için zaten bir giriş olduğunu unutmayın. 
Susan Amazon sitesinde gezinmeye devam ettikçe, her Web sayfası istediğinde tarayıcısı çerez dosyasına başvurur, bu site için kimlik numarasını alır ve HTTP isteğine kimlik numarasını içeren bir çerez başlık satırı koyar. 
Özellikle, Amazon sunucusuna yaptığı her HTTP isteği şu başlık satırını içerir:

`Cookie: 1678891298`

Bu şekilde, Amazon sunucusu Susan'ın Amazon sitesindeki etkinliğini takip edebilir. 
Amazon Web sitesi Susan'ın adını tam olarak bilmese de, 1678891298 numaralı kullanıcının hangi sayfaları, hangi sırayla ve hangi zamanlarda ziyaret ettiğini tam olarak bilir! Amazon, alışveriş sepeti hizmetini (**shopping cart service**) sağlamak için çerezleri kullanır—Amazon, Susan'ın satın almayı düşündüğü tüm ürünlerin bir listesini tutabilir, böylece oturum sonunda hepsini topluca ödeyebilir.

Susan bir hafta sonra Amazon sitesine geri dönerse, tarayıcısı istek mesajlarına `Cookie: 1678891298` başlık satırını eklemeye devam edecektir. 
Amazon ayrıca, Susan'a geçmişte Amazon'da ziyaret ettiği Web sayfalarına dayanarak ürünler önerir. 
Susan Amazon'a tam adını, e-posta adresini, posta adresini ve kredi kartı bilgilerini vererek kaydolursa, 
Amazon bu bilgileri veritabanına ekleyebilir ve böylece Susan'ın adını kimlik numarasıyla (ve geçmişte sitede ziyaret ettiği tüm sayfalarla!) ilişkilendirebilir. Amazon ve diğer e-ticaret siteleri "tek tıklamayla alışveriş" (**one-click shopping**) hizmetini bu şekilde sunar—Susan sonraki bir ziyarette bir ürün satın almayı seçtiğinde, adını, kredi kartı numarasını veya adresini tekrar girmesine gerek kalmaz.

Bu tartışmadan, çerezlerin bir kullanıcıyı tanımlamak için kullanılabileceğini görüyoruz. 
Bir kullanıcı bir siteyi ilk ziyaret ettiğinde, bir kullanıcı kimliği (muhtemelen adı) sağlayabilir. 
Sonraki oturumlarda, tarayıcı sunucuya bir çerez başlığı iletir ve böylece kullanıcıyı sunucuya tanıtır.
Çerezler böylece durumsuz HTTP'nin üzerine bir kullanıcı oturumu katmanı (**user session layer**) oluşturmak için kullanılabilir. 
Örneğin, bir kullanıcı Web tabanlı bir e-posta uygulamasına (**Web-based e-mail application**) (Hotmail gibi) giriş yaptığında, tarayıcı sunucuya çerez bilgisi gönderir ve sunucunun uygulamanın oturumu boyunca kullanıcıyı tanımlamasına olanak tanır.

Çerezler genellikle kullanıcı için internet alışveriş deneyimini basitleştirse de, gizlilik ihlali olarak da değerlendirilebildikleri için tartışmalıdırlar. 
Az önce gördüğümüz gibi, çerezler ve kullanıcı tarafından sağlanan hesap bilgilerinin bir kombinasyonunu kullanarak, bir Web sitesi bir kullanıcı hakkında çok şey öğrenebilir ve potansiyel olarak bu bilgiyi üçüncü bir tarafa (**third party**) satabilir.

#### Web Önbellekleme (Web Caching)

Bir Web önbelleği (**Web cache**)—aynı zamanda bir **proxy server (proxy sunucusu)** olarak da adlandırılır—bir kaynak Web sunucusu (**origin Web server**) adına HTTP isteklerini karşılayan bir ağ varlığıdır. Web önbelleğinin kendi disk depolama alanı (**disk storage**) vardır ve yakın zamanda istenen nesnelerin (**objects**) kopyalarını bu depolama alanında tutar. Bir kullanıcının tarayıcısı (**browser**), kullanıcının tüm HTTP isteklerinin ilk olarak Web önbelleğine yönlendirilecek şekilde yapılandırılabilir [RFC 7234]. Bir tarayıcı yapılandırıldıktan sonra, tarayıcının bir nesne için her isteği ilk olarak Web önbelleğine yönlendirilir. Örnek olarak, bir tarayıcının http://www.redberks.com/muck.gif nesnesini istediğini varsayalım. 

İşte olanlar:

1. Tarayıcı, Web önbelleğiyle bir TCP bağlantısı (**TCP connection**) kurar ve nesne için bir HTTP isteği (**HTTP request**) gönderir.
2. Web önbelleği, nesnenin yerel olarak depolanmış bir kopyasına sahip olup olmadığını kontrol eder. Varsa, Web önbelleği nesneyi bir HTTP yanıt mesajı (**HTTP response message**) içinde istemci tarayıcısına (**client browser**) döndürür.
3. Web önbelleğinde nesne yoksa, Web önbelleği kaynak sunucuya, yani www.redberks.com'a bir TCP bağlantısı açar. Web önbelleği daha sonra nesne için bir HTTP isteğini önbellekten sunucuya giden TCP bağlantısına (**cache-to-server TCP connection**) gönderir. Bu isteği aldıktan sonra, kaynak sunucu nesneyi bir HTTP yanıtı içinde Web önbelleğine gönderir.
4. Web önbelleği nesneyi aldığında, yerel depolama alanına (**local storage**) bir kopyasını kaydeder ve bir kopyayı, bir HTTP yanıt mesajı içinde, istemci tarayıcısına (istemci tarayıcısı ve Web önbelleği arasındaki mevcut TCP bağlantısı üzerinden) gönderir.

Bir önbelleğin aynı anda hem sunucu hem de istemci olduğunu unutmayın. Tarayıcılardan istek aldığında ve yanıt gönderdiğinde sunucudur. 
Kaynak sunucuya istek gönderdiğinde ve ondan yanıt aldığında ise istemcidir.

Tipik olarak bir Web önbelleği, bir İSS (**ISP**) tarafından satın alınır ve kurulur. 
Örneğin, bir üniversite kampüs ağına bir önbellek kurabilir ve tüm kampüs tarayıcılarını önbelleğe işaret edecek şekilde yapılandırabilir. 
Veya büyük bir konut İSS'si (Comcast gibi) ağına bir veya daha fazla önbellek kurabilir ve gönderdiği tarayıcıları kurulu önbelleklere işaret edecek şekilde önceden yapılandırabilir.

Web önbellekleme, iki nedenle İnternet'te yaygınlaşmıştır. Birincisi, bir Web önbelleği istemci isteği için yanıt süresini (**response time**) önemli ölçüde azaltabilir, özellikle istemci ve kaynak sunucu arasındaki darboğaz bant genişliği (**bottleneck bandwidth**) istemci ve önbellek arasındaki darboğaz bant genişliğinden çok daha azsa. İstemci ve önbellek arasında yüksek hızlı bir bağlantı varsa (ki genellikle böyledir) ve önbellekte istenen nesne varsa, önbellek nesneyi istemciye hızla teslim edebilir. İkincisi, yakında bir örnekle göstereceğimiz gibi, Web önbellekleri bir kurumun İnternet'e erişim bağlantısındaki trafiği önemli ölçüde azaltabilir. Trafiği azaltarak, kurum (örneğin, bir şirket veya bir üniversite) bant genişliğini o kadar hızlı yükseltmek zorunda kalmaz, böylece maliyetleri azaltır. Ayrıca, Web önbellekleri bir bütün olarak İnternet'teki Web trafiğini önemli ölçüde azaltabilir, böylece tüm uygulamalar için performansı artırır.

Önbelleklerin faydalarını daha derinlemesine anlamak için, Bir örnek düşünelim, iki ağ tane var—kurumsal ağı ve halka açık İnternet'in geri kalanı.
Kurumsal ağ yüksek hızlı bir LAN'dır (**LAN**). Kurumsal ağdaki bir yönlendirici (**router**) ve İnternet'teki bir yönlendirici, 15 Mbps'lik bir bağlantıyla bağlanmıştır. Kaynak sunucular İnternet'e bağlıdır ancak dünyanın her yerine dağılmış durumdadır.
Ortalama nesne boyutunun 1 Mbits olduğunu ve kurumun tarayıcılarından kaynak sunuculara olan ortalama istek hızının saniyede 15 istek olduğunu varsayalım. 
HTTP istek mesajlarının ihmal edilebilir derecede küçük olduğunu ve bu nedenle ağlarda veya erişim bağlantısında (kurumsal yönlendiriciden İnternet yönlendiricisine) trafik oluşturmadığını varsayalım. Ayrıca erişim bağlantısının İnternet tarafındaki yönlendiricinin bir HTTP isteğini (bir IP datagramı içinde) ilettiği andan yanıtı (tipik olarak birçok IP datagramı içinde) aldığı ana kadar geçen sürenin ortalama iki saniye olduğunu varsayalım. 
Gayri resmi olarak, bu son gecikmeyi "İnternet gecikmesi" (**Internet delay**) olarak adlandırıyoruz.

Toplam yanıt süresi—yani, tarayıcının bir nesneyi istemesinden nesneyi almasına kadar geçen süre—LAN gecikmesi (**LAN delay**), erişim gecikmesi (**access delay**) (yani, iki yönlendirici arasındaki gecikme) ve İnternet gecikmesinin toplamıdır. Şimdi bu gecikmeyi tahmin etmek için çok kaba bir hesaplama yapalım.

LAN üzerindeki trafik yoğunluğu (**traffic intensity**) 

```
(15 istek/sn) * (1 Mbits/istek) / (100 Mbps) = 0.15
```

iken, erişim bağlantısı üzerindeki trafik yoğunluğu (İnternet yönlendiricisinden kurumsal yönlendiriciye)

```
(15 istek/sn) * (1 Mbits/istek) / (15 Mbps) = 1
```

Bir LAN üzerindeki 0.15'lik bir trafik yoğunluğu genellikle en fazla on milisaniyelik gecikmeye neden olur; bu nedenle LAN gecikmesini ihmal edebiliriz. 
Ancak, trafik yoğunluğu 1'e yaklaştığında (erişim bağlantısı durumunda olduğu gibi), bir bağlantıdaki gecikme çok büyük olur ve sınırsız artar. 
Bu nedenle, istekleri karşılamak için ortalama yanıt süresi dakikalar mertebesinde olacaktır, hatta daha fazla olabilir, bu da kurumun kullanıcıları için kabul edilemezdir. Açıkçası bir şeyler yapılmalıdır.

Bir olası çözüm, erişim hızını 15 Mbps'den örneğin 100 Mbps'ye çıkarmaktır. Bu, erişim bağlantısındaki trafik yoğunluğunu 0.15'e düşürecektir, bu da iki yönlendirici arasında ihmal edilebilir gecikmelere dönüşür. Bu durumda, toplam yanıt süresi kabaca iki saniye, yani İnternet gecikmesi olacaktır. 
Ancak bu çözüm aynı zamanda kurumun erişim bağlantısını 15 Mbps'den 100 Mbps'ye yükseltmesi gerektiği anlamına gelir, bu da maliyetli bir öneridir.

Şimdi erişim bağlantısını yükseltmeyip bunun yerine kurumsal ağa bir Web önbelleği kurma alternatif çözümünü düşünelim. 
İsabet oranları (**Hit rates**)—bir önbellek tarafından karşılanan isteklerin oranı—pratikte tipik olarak 0.2 ila 0.7 arasında değişir. 
Örnek olması açısından, bu kurum için önbelleğin %0.4'lük bir isabet oranı sağladığını varsayalım.
İstemciler ve önbellek aynı yüksek hızlı LAN'a bağlı olduğu için, isteklerin %40'ı neredeyse anında, örneğin 10 milisaniye içinde, önbellek tarafından karşılanacaktır. Bununla birlikte, isteklerin kalan %60'ı hala kaynak sunucular tarafından karşılanmalıdır. 
Ancak istenen nesnelerin sadece %60'ı erişim bağlantısından geçtiğinde, erişim bağlantısındaki trafik yoğunluğu 1.0'dan 0.6'ya düşer. 
Tipik olarak, 0.8'den düşük bir trafik yoğunluğu, 15 Mbps'lik bir bağlantıda düşük bir gecikmeye, örneğin on milisaniyelik bir gecikmeye karşılık gelir. 
Bu gecikme, iki saniyelik İnternet gecikmesiyle karşılaştırıldığında ihmal edilebilir düzeydedir. 

Bu hususlar göz önüne alındığında, ortalama gecikme bu nedenle şöyledir:

```
0.4 * (0.01 saniye) + 0.6 * (2.01 saniye)
```

Bu, 1.2 saniyeden biraz daha fazladır. Dolayısıyla, bu ikinci çözüm, ilk çözümden daha da düşük bir yanıt süresi sağlar ve kurumun İnternet'e olan bağlantısını yükseltmesini gerektirmez. Kurumun elbette bir Web önbelleği satın alması ve kurması gerekir. Ancak bu maliyet düşüktür—birçok önbellek, ucuz PC'lerde çalışan kamu malı yazılımları kullanır.

İçerik Dağıtım Ağları (CDN'ler) (**Content Distribution Networks (CDNs)**) aracılığıyla, Web önbellekleri İnternet'te giderek daha önemli bir rol oynamaktadır. Bir CDN şirketi, İnternet genelinde birçok coğrafi olarak dağıtılmış önbellek kurar, böylece trafiğin büyük bir kısmını yerelleştirir. Paylaşılan CDN'ler (Akamai ve Limelight gibi) ve özel CDN'ler (Google ve Netflix gibi) vardır. 

#### Koşullu GET (The Conditional GET)

Önbellekleme (**caching**) kullanıcı tarafından algılanan yanıt sürelerini azaltabilse de, yeni bir sorun ortaya çıkarır—önbellekte bulunan bir nesnenin kopyası bayat (**stale**) olabilir. Başka bir deyişle, Web sunucusunda barındırılan nesne, istemcide önbelleğe alındığından beri değiştirilmiş olabilir. 
Neyse ki, HTTP'nin bir önbelleğin nesnelerinin güncel olduğunu doğrulamasını sağlayan bir mekanizması vardır. 
Bu mekanizmaya **koşullu GET (conditional GET)** [RFC 7232] denir. 
Bir HTTP istek mesajı (**HTTP request message**) şu durumlarda sözde koşullu GET mesajıdır: (1) istek mesajı GET methodunu kullanıyorsa ve (2) istek mesajı bir `If-Modified-Since:` başlık satırı içeriyorsa.

Koşullu GET'in nasıl çalıştığını göstermek için bir örnek üzerinden geçelim. 
İlk olarak, istekte bulunan bir tarayıcı adına, bir proxy önbellek (**proxy cache**) bir Web sunucusuna bir istek mesajı gönderir:

```

GET /computer/hp.gif HTTP/1.1
Host: [www.redberks.com](https://www.google.com/search?q=https://www.redberks.com)

```

İkinci olarak, Web sunucusu istenen nesne ile birlikte önbelleğe bir yanıt mesajı (**response message**) gönderir:

```

HTTP/1.1 200 OK
Date: Sat, 3 Oct 2025 15:39:29
Server: Apache/1.3.0 (Unix)
Last-Modified: Wed, 9 Sep 2025 09:23:24
Content-Type: image/gif
(data data data data data ...)

```

Önbellek nesneyi istekte bulunan tarayıcıya iletir, ancak aynı zamanda nesneyi yerel olarak önbelleğe alır. 
Daha da önemlisi, önbellek nesneyle birlikte son değiştirilme tarihini (**last-modified date**) de saklar. 
Üçüncü olarak, bir hafta sonra başka bir tarayıcı aynı nesneyi önbellek aracılığıyla ister ve nesne hala önbellektedir. 
Bu nesnenin geçen hafta Web sunucusunda değiştirilmiş olabileceği için, önbellek bir koşullu GET göndererek bir güncellik kontrolü yapar. 
Özellikle, önbellek şunu gönderir:

```

GET /computer/hp.gif  HTTP/1.1
Host: [www.redberks.com](https://www.google.com/search?q=https://www.redberks.com)
If-modified-since: Wed, 9 Sep 2025 09:23:24

```

`If-modified-since:` başlık satırının değerinin, bir hafta önce sunucu tarafından gönderilen `Last-Modified:` başlık satırının değeriyle tam olarak aynı olduğuna dikkat edin. Bu koşullu GET, sunucuya nesneyi yalnızca belirtilen tarihten sonra değiştirildiyse göndermesini söyler. Nesnenin `9 Eylül 2025 09:23:24`'ten beri değiştirilmediğini varsayalım. Ardından, dördüncü olarak, Web sunucusu önbelleğe bir yanıt mesajı gönderir:

```

HTTP/1.1 304 Not Modified
Date: Sat, 10 Oct 2025 15:39:29
Server: Apache/1.3.0 (Unix)
(empty entity body)

```

Koşullu GET'e yanıt olarak, Web sunucusunun hala bir yanıt mesajı gönderdiğini ancak yanıt mesajına istenen nesneyi dahil etmediğini görüyoruz. 
İstenen nesneyi dahil etmek yalnızca bant genişliğini (**bandwidth**) boşa harcar ve kullanıcı tarafından algılanan yanıt süresini (**user-perceived response time**) artırır, özellikle nesne büyükse. Bu son yanıt mesajının durum satırında (**status line**) `304 Not Modified` yazdığına dikkat edin, bu da önbelleğe (proxy önbelleğinin (**proxy cache’s**) ) önbelleğe alınmış kopyasını istekte bulunan tarayıcıya iletebileceğini söyler.

#### HTTP/2

2015 yılında standartlaştırılan HTTP/2 [RFC 7540], 1997'de standartlaştırılan HTTP/1.1'den sonraki ilk yeni HTTP versiyonu oldu. 
Standartlaşmadan bu yana HTTP/2 hızla benimsendi; 2020'de en popüler 10 milyon web sitesinin %40'ından fazlası HTTP/2'yi destekliyordu [W3Techs]. 
Google Chrome, Internet Explorer, Safari, Opera ve Firefox dahil olmak üzere çoğu tarayıcı da HTTP/2'yi desteklemektedir.

HTTP/2'nin birincil hedefleri, tek bir TCP bağlantısı (**single TCP connection**) üzerinden istek ve yanıt çoklamayı (**request and response multiplexing**) etkinleştirerek algılanan gecikmeyi (**latency**) azaltmak, istek önceliklendirme (**request prioritization**) ve sunucu itme (**server push**) sağlamak ve HTTP başlık alanlarının (**HTTP header fields**) verimli sıkıştırılmasını sağlamaktır. HTTP/2, HTTP methodlarını, durum kodlarını (**status codes**), URL'leri veya başlık alanlarını değiştirmez. Bunun yerine, HTTP/2 verinin istemci ve sunucu arasında nasıl formatlandığını ve taşındığını değiştirir.

HTTP/2 ihtiyacını anlamak için, HTTP/1.1'in kalıcı TCP bağlantıları (**persistent TCP connections**) kullandığını ve bir Web sayfasının sunucudan istemciye tek bir TCP bağlantısı üzerinden gönderilmesine olanak tanıdığını hatırlayın. Web sayfası başına yalnızca bir TCP bağlantısı olmasıyla, sunucudaki soket sayısı azalır ve taşınan her Web sayfası ağ bant genişliğinden (**network bandwidth**) adil bir pay alır (aşağıda tartışıldığı gibi). 
Ancak Web tarayıcısı geliştiricileri, bir Web sayfasındaki tüm nesneleri tek bir TCP bağlantısı üzerinden göndermenin Birleştirme Başlangıcı (Head of Line - HOL) engelleme sorunu (**Head of Line (HOL) blocking problem**) olduğunu hızla keşfetti. 
HOL engellemesini anlamak için, bir HTML temel sayfası, Web sayfasının üst kısmına yakın büyük bir video klibi ve videonun altında birçok küçük nesne içeren bir Web sayfası düşünün. Ayrıca, sunucu ile istemci arasındaki yolda düşük-orta hızlı bir darboğaz bağlantısı (**bottleneck link**) (örneğin, düşük hızlı bir kablosuz bağlantı (**low-speed wireless link**)) olduğunu varsayalım. Tek bir TCP bağlantısı kullanılarak, video klibi darboğaz bağlantısından geçerken uzun zaman alacak, küçük nesneler ise video klibin arkasında beklerken gecikecektir; yani, sıranın başındaki video klibi arkasındaki küçük nesneleri engellemektedir. 
HTTP/1.1 tarayıcıları tipik olarak birden çok paralel TCP bağlantısı (**parallel TCP connections**) açarak bu sorunu aşar, böylece aynı web sayfasındaki nesnelerin tarayıcıya paralel olarak gönderilmesini sağlarlar. Bu şekilde, küçük nesneler tarayıcıya çok daha hızlı ulaşabilir ve işlenebilir, böylece kullanıcı tarafından algılanan gecikme azalır.

Ayrıntılı olarak tartışılan TCP tıkanıklık kontrolü (**TCP congestion control**), tarayıcılara tek bir kalıcı bağlantı yerine birden çok paralel TCP bağlantısı kullanmak için istenmeyen bir teşvik de sağlar. Çok kaba bir ifadeyle, TCP tıkanıklık kontrolü, bir darboğaz bağlantısını paylaşan her TCP bağlantısına o bağlantının mevcut bant genişliğinden (**link bandwidth**) eşit bir pay vermeyi amaçlar; bu nedenle, bir darboğaz bağlantısı üzerinden çalışan n TCP bağlantısı varsa, her bağlantı bant genişliğinin yaklaşık 1/n'sini alır. Tek bir Web sayfasını taşımak için birden çok paralel TCP bağlantısı açarak, tarayıcı "hile yapabilir" ve bağlantı bant genişliğinden daha büyük bir pay alabilir. Birçok HTTP/1.1 tarayıcısı, yalnızca HOL engellemesini atlatmakla kalmayıp aynı zamanda daha fazla bant genişliği elde etmek için altıya kadar paralel TCP bağlantısı açar.

HTTP/2'nin birincil hedeflerinden biri, tek bir Web sayfasını taşımak için paralel TCP bağlantılarından kurtulmak (veya en azından sayılarını azaltmak) tır. 
Bu, sunucularda açılması ve sürdürülmesi gereken soket sayısını azaltmakla kalmaz, aynı zamanda TCP tıkanıklık kontrolünün amaçlandığı gibi çalışmasına da olanak tanır. Ancak bir Web sayfasını taşımak için yalnızca bir TCP bağlantısıyla, HTTP/2'nin HOL engellemesini önlemek için dikkatlice tasarlanmış mekanizmalara ihtiyacı vardır.

#### HTTP/2 Çerçeveleme (Framing)

HTTP/2'nin HOL engelleme (**HOL blocking**) çözümü, her mesajı küçük çerçevelere (**frames**) bölmek ve aynı TCP bağlantısı (**TCP connection**) üzerinde istek ve yanıt mesajlarını araya almaktır (**interleave**). Bunu anlamak için, bir büyük video klip ve örneğin 8 küçük nesneden oluşan bir Web sayfası örneğini tekrar ele alalım. Dolayısıyla, bu Web sayfasını görmek isteyen herhangi bir tarayıcıdan sunucu 9 eşzamanlı istek alacaktır. 
Bu isteklerin her biri için sunucunun tarayıcıya 9 rakip HTTP yanıt mesajı göndermesi gerekir. 
Tüm çerçevelerin sabit uzunlukta olduğunu, video klibin 1000 çerçeveden oluştuğunu ve küçük nesnelerin her birinin iki çerçeveden oluştuğunu varsayalım. 
Çerçeve araya alma (**interleave**) ile, video klibinden bir çerçeve gönderdikten sonra, küçük nesnelerin her birinin ilk çerçeveleri gönderilir. 
Ardından video klibin ikinci çerçevesini gönderdikten sonra, küçük nesnelerin her birinin son çerçeveleri gönderilir. 
Böylece, tüm küçük nesneler toplam 18 çerçeve gönderildikten sonra gönderilir. Eğer araya alma kullanılmasaydı, küçük nesneler ancak 1016 çerçeve gönderildikten sonra gönderilebilirdi. Bu nedenle HTTP/2 çerçeveleme mekanizması (**framing mechanism**) kullanıcı tarafından algılanan gecikmeyi (**user-perceived delay**) önemli ölçüde azaltabilir.

Bir HTTP mesajını bağımsız çerçevelere bölme, araya alma ve ardından diğer uçta yeniden birleştirme yeteneği, HTTP/2'nin en önemli geliştirmesidir. 
Çerçeveleme, HTTP/2 protokolünün çerçeveleme alt katmanı (**framing sub-layer**) tarafından yapılır. 
Bir sunucu bir HTTP yanıtı göndermek istediğinde, yanıt çerçeveleme alt katmanı tarafından işlenir ve burada çerçevelere ayrılır. 
Yanıtın başlık alanı (**header field**) bir çerçeve olur ve mesajın gövdesi (**body**) bir veya daha fazla ek çerçeveye ayrılır. 
Yanıtın çerçeveleri daha sonra sunucudaki çerçeveleme alt katmanı tarafından diğer yanıtların çerçeveleriyle araya alınır ve tek kalıcı TCP bağlantısı üzerinden gönderilir. Çerçeveler istemciye ulaştığında, ilk olarak çerçeveleme alt katmanında orijinal yanıt mesajlarına yeniden birleştirilir ve ardından tarayıcı tarafından her zamanki gibi işlenir. Benzer şekilde, bir istemcinin HTTP istekleri de çerçevelere ayrılır ve araya alınır.

Her HTTP mesajını bağımsız çerçevelere bölmenin yanı sıra, çerçeveleme alt katmanı çerçeveleri ikili olarak da kodlar (**binary encodes**). 
İkili protokoller (**binary protocols**), ayrıştırması (**parse**) daha verimlidir, biraz daha küçük çerçevelere yol açar ve hatalara daha az eğilimlidir.

#### Yanıt Mesajı Önceliklendirme ve Sunucu İtme (Server Pushing)

Mesaj önceliklendirme (**Message prioritization**), geliştiricilerin (**developers**) uygulama performansını (**application performance**) daha iyi optimize etmek için isteklerin göreceli önceliğini özelleştirmelerine olanak tanır. Az önce öğrendiğimiz gibi, çerçeveleme alt katmanı (**framing sub-layer**), aynı isteyiciye (**requestor**) yönelik paralel veri akışları (**parallel streams of data**) halinde mesajlar düzenler. 
Bir istemci sunucuya eşzamanlı istekler (**concurrent requests**) gönderdiğinde, her mesaja 1 ila 256 arasında bir ağırlık (**weight**) atayarak istediği yanıtları (**responses**) önceliklendirebilir (**prioritize**). Daha yüksek sayı daha yüksek önceliği gösterir. Sunucu bu ağırlıkları kullanarak en yüksek önceliğe sahip yanıtlar için çerçeveleri önce gönderebilir. Buna ek olarak, istemci ayrıca, bağlı olduğu mesajın kimliğini belirterek her mesajın diğer mesajlara olan bağımlılığını (**message’s dependency**) da belirtir.

HTTP/2'nin bir diğer özelliği, bir sunucunun tek bir istemci isteği (**single client request**) için birden fazla yanıt (**response**) gönderebilmesidir. 
Yani, orijinal isteğe (**original request**) verilen yanıta ek olarak, sunucu istemcinin her birini talep etmek zorunda kalmadan istemciye ek nesneleri itebilir (**push additional objects**). Bu, HTML temel sayfasının (**HTML base page**) Web sayfasını tamamen oluşturmak (**render the Web page**) için gerekli olacak nesneleri belirtmesi sayesinde mümkündür. Dolayısıyla, bu nesneler için HTTP isteklerini (**HTTP requests**) beklemek yerine, sunucu HTML sayfasını analiz edebilir (**analyze**), gerekli nesneleri belirleyebilir ve bu nesneler için açık istekler (**explicit requests**) almadan önce bunları istemciye gönderebilir. Sunucu itme (**Server push**), açık istekleri beklemeden kaynaklanan ek gecikmeyi (**latency**) ortadan kaldırır.

#### HTTP/3

İlerleyen konularda ele alınan QUIC, yalın UDP protokolü üzerinde uygulama katmanında (**application layer**) uygulanan yeni bir "taşıma" protokolüdür (**transport protocol**). QUIC, mesaj çoklama (araya alma) (**message multiplexing (interleaving)**), akış başına akış kontrolü (**per-stream flow control**) ve düşük gecikmeli bağlantı kurma (**low-latency connection establishment**) gibi HTTP için arzu edilen çeşitli özelliklere sahiptir. HTTP/3, QUIC üzerinde çalışmak üzere tasarlanmış yepyeni bir HTTP protokolüdür (**HTTP protocol**). 2020 itibarıyla HTTP/3, İnternet taslaklarında (**Internet drafts**) açıklanmıştır ve henüz tam olarak standartlaştırılmamıştır (**standardized**). HTTP/2 özelliklerinin (**HTTP/2 features**) çoğu (mesaj araya alma gibi) QUIC tarafından üstlenilmiştir, bu da HTTP/3 için daha basit ve modern bir tasarım sağlamıştır.

## İnternette Elektronik Posta

Elektronik posta, İnternet'in başlangıcından beri mevcuttur. İnternet bebeklik dönemindeyken en popüler uygulamaydı [Segaller 1998] ve yıllar içinde daha karmaşık ve güçlü hale geldi. İnternet'in en önemli ve en çok kullanılan uygulamalarından biri olmaya devam etmektedir.

Sıradan posta gibi, e-posta da eşzamansız bir iletişim ortamıdır—insanlar mesajları kendileri için uygun olduğunda gönderir ve okur, diğer insanların programlarıyla koordinasyon sağlamak zorunda kalmazlar. Postanın aksine, elektronik posta hızlıdır, dağıtımı kolaydır ve ucuzdur. 
Modern e-posta, ekli mesajlar (**messages with attachments**), köprü bağlantılar (**hyperlinks**), HTML formatlı metin (**HTML-formatted text**) ve gömülü fotoğraflar gibi birçok güçlü özelliğe sahiptir.

Bu bölümde, İnternet e-postasının kalbinde yer alan uygulama katmanı protokollerini (**application-layer protocols**) inceleyeceğiz. 
Ancak bu protokollerin derinlemesine tartışmasına dalmadan önce, İnternet posta sistemine ve temel bileşenlerine üst düzey bir bakış atalım.

İnternet posta sistemine üst düzey bir bakış, üç ana bileşenden oluşur: kullanıcı ajanları (**user agents**), posta sunucuları (**mail servers**) ve Basit Posta Transfer Protokolü (SMTP) (**Simple Mail Transfer Protocol (SMTP)**). 
Şimdi bu bileşenlerin her birini, gönderen Alice'in, alıcı Bob'a bir e-posta mesajı (**e-mail message**) gönderdiği bağlamda açıklayalım. 
Kullanıcı ajanları, kullanıcıların mesajları okumasına (**read**), yanıtlamasına (**reply to**), iletmesine (**forward**), kaydetmesine (**save**) ve oluşturmasına (**compose messages**) olanak tanır. E-posta için kullanıcı ajanlarına örnek olarak Microsoft Outlook, Apple Mail, Web tabanlı Gmail (**Web-based Gmail**), bir akıllı telefonda (**smartphone**) çalışan Gmail Uygulaması (**Gmail App**) vb. verilebilir. 
Alice mesajını oluşturmayı bitirdiğinde (**composing her message**), kullanıcı ajanı mesajı kendi posta sunucusuna gönderir ve mesaj orada posta sunucusunun giden mesaj kuyruğuna (**outgoing message queue**) yerleştirilir. Bob bir mesajı okumak istediğinde, kullanıcı ajanı mesajı kendi posta sunucusundaki posta kutusundan (**mailbox**) alır.

Posta sunucuları, e-posta altyapısının çekirdeğini oluşturur. Bob gibi her alıcının, posta sunucularından birinde bulunan bir posta kutusu vardır. 
Bob'un posta kutusu, kendisine gönderilen mesajları yönetir ve saklar. Tipik bir mesaj yolculuğuna gönderenin kullanıcı ajanında başlar, sonra gönderenin posta sunucusuna gider ve ardından alıcının posta sunucusuna giderek alıcının posta kutusuna bırakılır. 
Bob, posta kutusundaki mesajlara erişmek istediğinde, posta kutusunu içeren posta sunucusu Bob'u (kullanıcı adı (**username**) ve şifresiyle (**password**)) doğrular. Alice'in posta sunucusu ayrıca Bob'un posta sunucusundaki hatalarla da başa çıkmalıdır. 
Alice'in sunucusu Bob'un sunucusuna posta teslim edemezse, Alice'in sunucusu mesajı bir mesaj kuyruğunda (**message queue**) bekletir ve daha sonra mesajı transfer etmeye çalışır. Yeniden denemeler genellikle 30 dakika kadar aralıklarla yapılır; birkaç gün sonra başarı sağlanamazsa, sunucu mesajı siler ve gönderene (Alice'e) bir e-posta mesajıyla bildirir.

SMTP, İnternet elektronik postası için ana uygulama katmanı protokolüdür (**application-layer protocol**). 
Postayı gönderenin posta sunucusundan alıcının posta sunucusuna transfer etmek için TCP'nin güvenilir veri transferi hizmetini (**reliable data transfer service of TCP**) kullanır. Çoğu uygulama katmanı protokolü gibi, SMTP'nin de iki tarafı vardır: gönderenin posta sunucusunda çalışan bir istemci tarafı (**client side**) ve alıcının posta sunucusunda çalışan bir sunucu tarafı (**server side**).
SMTP'nin hem istemci hem de sunucu tarafları her posta sunucusunda çalışır. Bir posta sunucusu diğer posta sunucularına posta gönderdiğinde, bir SMTP istemcisi gibi davranır. Bir posta sunucusu diğer posta sunucularından posta aldığında, bir SMTP sunucusu gibi davranır.

#### SMTP

RFC 5321'de tanımlanan SMTP, İnternet elektronik postasının kalbinde yer alır. 
Yukarıda belirtildiği gibi, SMTP mesajları gönderenlerin posta sunucularından (**mail servers**) alıcıların posta sunucularına aktarır. 
SMTP, HTTP'den çok daha eskidir. (Orijinal SMTP RFC'si 1982'ye kadar uzanır ve SMTP ondan çok daha önce de vardı.) 
İnternet'teki yaygınlığı ile kanıtlandığı gibi SMTP'nin çok sayıda harika özelliği olmasına rağmen, yine de belirli arkaik özelliklere sahip eski bir teknolojidir. Örneğin, tüm posta mesajlarının gövdesini (**body**) (yalnızca başlıkları (**headers**) değil) basit 7 bit ASCII ile sınırlar. 
Bu kısıtlama, iletim kapasitesinin az olduğu ve kimsenin büyük ekler veya büyük resim, ses veya video dosyaları e-postalamadığı 1980'lerin başlarında mantıklıydı. Ancak bugün, multimedya çağında, 7 bit ASCII kısıtlaması biraz sıkıntılıdır—binary multimedya verilerinin SMTP üzerinden gönderilmeden önce ASCII'ye kodlanmasını gerektirir; ve karşılık gelen ASCII mesajının SMTP aktarımından sonra tekrar binary decode edilmesini gerektirir. 
Hatırlayın ki HTTP, multimedya verilerinin aktarımdan önce ASCII kodlanmasını gerektirmez.

SMTP'nin temel işleyişini göstermek için yaygın bir senaryoyu adım adım inceleyelim. 
Alice'in Bob'a basit bir ASCII mesajı göndermek istediğini varsayalım.

1. Alice e-posta için kullanıcı ajanını (**user agent**) çalıştırır, Bob'un e-posta adresini (**e-mail address**) sağlar (örneğin, bob@gmail.com), bir mesaj oluşturur ve kullanıcı ajanına mesajı göndermesi talimatını verir.
2. Alice'in kullanıcı ajanı mesajı posta sunucusuna gönderir ve mesaj orada bir mesaj kuyruğuna (**message queue**) yerleştirilir.
3. Alice'in posta sunucusunda çalışan SMTP istemci tarafı (**client side**), mesajı mesaj kuyruğunda görür. Bob'un posta sunucusunda çalışan bir SMTP sunucusuna (**SMTP server**) bir TCP bağlantısı (**TCP connection**) açar.
4. Bazı başlangıç SMTP el sıkışmasından (**SMTP handshaking**) sonra, SMTP istemcisi Alice'in mesajını TCP bağlantısına gönderir.
5. Bob'un posta sunucusunda, SMTP'nin sunucu tarafı (**server side**) mesajı alır. Bob'un posta sunucusu daha sonra mesajı Bob'un posta kutusuna (**mailbox**) yerleştirir.
6. Bob, uygun olduğunda mesajı okumak için kullanıcı ajanını çalıştırır.

İki posta sunucusu dünyanın zıt uçlarnda bulunsa bile, SMTP'nin normalde posta göndermek için ara posta sunucularını (**intermediate mail servers**) kullanmadığını gözlemlemek önemlidir. Alice'in sunucusu Hong Kong'da ve Bob'un sunucusu St. Louis'de ise, TCP bağlantısı Hong Kong ve St. Louis sunucuları arasında doğrudan bir bağlantıdır. Özellikle, Bob'un posta sunucusu kapalıysa, mesaj Alice'in posta sunucusunda kalır ve yeni bir deneme bekler—mesaj herhangi bir ara posta sunucusuna yerleştirilmez.

Şimdi SMTP'nin bir mesajı gönderen posta sunucusundan alan posta sunucusuna nasıl aktardığına daha yakından bakalım. 
SMTP protokolünün, yüz yüze insan etkileşimleri için kullanılan protokollere birçok benzerliği olduğunu göreceğiz. 
İlk olarak, istemci SMTP (gönderen posta sunucusu ana bilgisayarında çalışıyor), alan posta sunucusu ana bilgisayarında çalışan sunucu SMTP'sinde 25 numaralı porta bir bağlantı kurması için TCP'ye talimat verir. Sunucu kapalıysa, istemci daha sonra tekrar dener. 
Bu bağlantı kurulduktan sonra, sunucu ve istemci bir uygulama katmanı el sıkışması (**application-layer handshaking**) gerçekleştirir—tıpkı insanların birinden diğerine bilgi aktarmadan önce genellikle kendilerini tanıttığı gibi, SMTP istemcileri ve sunucuları bilgi aktarmadan önce kendilerini tanıtırlar. 
Bu SMTP el sıkışma aşamasında, SMTP istemcisi gönderenin (mesajı oluşturan kişinin) e-posta adresini ve alıcının e-posta adresini belirtir. 
SMTP istemcisi ve sunucusu birbirlerine kendilerini tanıttıktan sonra, istemci mesajı gönderir. 
SMTP, mesajı sunucuya hatasız ulaştırmak için TCP'nin güvenilir veri transferi hizmetine güvenebilir. 
İstemci, sunucuya göndermesi gereken başka mesajları varsa, aynı TCP bağlantısı üzerinden bu işlemi tekrarlar; aksi takdirde, TCP'ye bağlantıyı kapatması talimatını verir.

Şimdi bir SMTP istemcisi (C) ve bir SMTP sunucusu (S) arasında değiş tokuş edilen mesajların örnek bir dökümüne göz atalım. 
İstemcinin ana bilgisayar adı redberks.tr ve sunucunun ana bilgisayar adı sakarya.edu'dur. 
C: ile başlayan ASCII metin satırları, istemcinin TCP soketine tam olarak gönderdiği satırlardır ve S: ile başlayan ASCII metin satırları, sunucunun TCP soketine tam olarak gönderdiği satırlardır. Aşağıdaki döküm, TCP bağlantısı kurulur kurulmaz başlar.

```
S: 220 sakarya.edu
C: HELO redberks.tr
S: 250 Hello redberks.tr, pleased to meet you
C: MAIL FROM: [email address removed]
S: 250 [email address removed] ... Sender ok
C: RCPT TO: [email address removed]
S: 250 [email address removed] ... Recipient ok
C: DATA
S: 354 Enter mail, end with "." on a line by itself
C: Her şey yolunda mı?
C: Gelmem gerekiyor mu?
C: .
S: 250 Message accepted for delivery
C: QUIT
S: 221 sakarya.edu closing connection
````

Yukarıdaki örnekte, istemci redberks.tr posta sunucusundan sakarta.edu posta sunucusuna bir mesaj ("Her şey yolunda mı? Gelmem gerekiyor mu?") göndermektedir. Diyaloğun bir parçası olarak, istemci beş komut yayınladı: HELO(HELLO KISA), MAIL FROM, RCPT TO, DATA ve QUIT. Bu komutlar kendi kendini açıklayıcıdır. 
İstemci ayrıca sunucuya mesajın sonunu belirten tek bir noktadan oluşan bir satır gönderir. (ASCII jargonunda, her mesaj CRLF.CRLF ile biter, burada CR ve LF sırasıyla satır başı (**carriage return**) ve satır besleme (**line feed**) anlamına gelir.) Sunucu, her komuta bir yanıt kodu (**reply code**) ve bazı (isteğe bağlı) İngilizce açıklamalar içeren yanıtlar yayınlar. Burada SMTP'nin kalıcı bağlantılar (**persistent connections**) kullandığını belirtmek gerekir: Eğer gönderen posta sunucusunun aynı alan posta sunucusuna göndermesi gereken birden fazla mesaj varsa, tüm mesajları aynı TCP bağlantısı üzerinden gönderebilir. 
Her mesaj için, istemci süreci yeni bir `MAIL FROM: redberks.tr` ile başlatır, mesajın sonunu bağımsız bir nokta ile belirtir ve tüm mesajlar gönderildikten sonra QUIT komutunu verir.

Bir SMTP sunucusuyla doğrudan bir diyalog kurmak için Telnet kullanmanız şiddetle tavsiye edilir. Bunu yapmak için şunu yazın:

```bash
telnet smtp.gmail.com 25
````

Burada `smtp.gmail.com`, yerel bir posta sunucusunun (**local mail server**) adıdır. Bunu yaptığınızda, yerel ana bilgisayarınız (**local host**) ile posta sunucusu arasında sadece bir TCP bağlantısı kurmuş olursunuz. Bu satırı yazdıktan sonra, sunucudan hemen 220 yanıtını almalısınız. 
Ardından, uygun zamanlarda SMTP komutları olan HELO, MAIL FROM, RCPT TO, DATA, CRLF.CRLF ve QUIT komutlarını yayınlayın. 

#### Posta Mesaj Formatları

Alice, Bob'a sıradan bir posta mektubu (**snail-mail letter**) yazdığında, mektubun üst kısmına Bob'un adresi, kendi iade adresi (**return address**) ve tarih gibi her türlü ek başlık bilgisini (**peripheral header information**) ekleyebilir. Benzer şekilde, bir e-posta mesajı (**e-mail message**) bir kişiden diğerine gönderildiğinde, mesajın gövdesinden (**body**) önce ek bilgi içeren bir başlık (**header**) gelir. Bu ek bilgi, RFC 5322'de tanımlanan bir dizi başlık satırı (**header lines**) içinde bulunur. Başlık satırları ve mesajın gövdesi boş bir satırla (**blank line**) (yani CRLF ile) ayrılır. 
RFC 5322, posta başlık satırlarının tam formatını ve anlamsal yorumlarını belirtir. HTTP'de olduğu gibi, her başlık satırı, bir anahtar kelimeyi (**keyword**) takiben iki nokta üst üste ve ardından bir değer içeren okunabilir metin içerir. Anahtar kelimelerin bazıları zorunlu, diğerleri ise isteğe bağlıdır. Her başlığın bir `From:` başlık satırı ve bir `To:` başlık satırı olmalıdır; bir başlık, bir `Subject:` başlık satırı ve diğer isteğe bağlı başlık satırlarını da içerebilir. Bu başlık satırlarının, incelediğimiz SMTP komutlarından (**SMTP commands**) farklı olduğunu (hatta "from" ve "to" gibi bazı ortak kelimeler içerseler bile) not etmek önemlidir. O bölümde yer alan komutlar, SMTP el sıkışma protokolünün (**SMTP handshaking protocol**) bir parçasıydı; bu bölümde incelenen başlık satırları ise posta mesajının kendisinin bir parçasıdır.

Tipik bir mesaj başlığı (**message header**) şöyle görünür:

```

From: [email address removed]
To: [email address removed]
Subject: Hal ve hatır sorma.

```

Mesaj başlığından sonra boş bir satır gelir; ardından mesaj gövdesi (ASCII olarak) gelir. Tartışıldığı gibi, `Subject:` başlık satırı da dahil olmak üzere bazı başlık satırları içeren bir mesajı bir posta sunucusuna göndermek için Telnet (**Telnet**) kullanmalısınız. Bunu yapmak için, `telnet serverName(herhangi bir server) 25` komutunu verin.

#### Posta Erişim Protokolleri

SMTP, mesajı Alice'in posta sunucusundan (**Alice’s mail server**) Bob'un posta sunucusuna (**Bob’s mail server**) teslim ettikten sonra, mesaj Bob'un posta kutusuna (**Bob’s mailbox**) yerleştirilir. 
Bob'un (alıcı) kullanıcı ajanını (**user agent**) yerel ana bilgisayarında (**local host**) (örneğin, akıllı telefonunda (**smartphone**) veya PC'sinde) çalıştırdığı düşünüldüğünde, yerel ana bilgisayarına bir posta sunucusu (**mail server**) da yerleştirmeyi düşünmek doğaldır. Bu yaklaşımla, Alice'in posta sunucusu Bob'un PC'si ile doğrudan iletişim kurardı. 
Ancak bu yaklaşımın bir sorunu var. Bir posta sunucusunun posta kutularını yönettiğini ve SMTP'nin istemci ve sunucu taraflarını çalıştırdığını hatırlayın. 
Eğer Bob'un posta sunucusu yerel ana bilgisayarında olsaydı, Bob'un ana bilgisayarının yeni posta almak için sürekli açık kalması ve İnternet'e bağlı olması gerekirdi, ki yeni posta her an gelebilir. 
Bu birçok İnternet kullanıcısı için pratik değildir. Bunun yerine, tipik bir kullanıcı yerel ana bilgisayarında bir kullanıcı ajanı çalıştırır, ancak posta kutusuna her zaman açık, paylaşılan bir posta sunucusunda (**always on shared mail server**) saklanan posta kutusuna erişir. Bu posta sunucusu diğer kullanıcılarla paylaşılır.

Şimdi bir e-posta mesajının Alice'ten Bob'a gönderilirken izlediği yolu düşünelim. Az önce öğrendik ki yol boyunca bir noktada e-posta mesajının Bob'un posta sunucusuna bırakılması gerekiyor. 
Bu, Alice'in kullanıcı ajanının (**sender’s user agent**) mesajı doğrudan Bob'un posta sunucusuna göndermesiyle basitçe yapılabilirdi. Ancak, tipik olarak gönderenin kullanıcı ajanı doğrudan alıcının posta sunucusuyla iletişim kurmaz. Bunun yerine, Alice'in kullanıcı ajanı, e-posta mesajını kendi posta sunucusuna teslim etmek için SMTP veya HTTP kullanır, ardından Alice'in posta sunucusu SMTP'yi (bir SMTP istemcisi olarak) kullanarak e-posta mesajını Bob'un posta sunucusuna iletir. Neden iki adımlı prosedür (**two-step procedure**)? Esas olarak Alice'in posta sunucusu aracılığıyla iletilmeden, Alice'in kullanıcı ajanının ulaşılamayan hedef posta sunucusuna (**unreachable destination mail server**) karşı herhangi bir çaresi olmaması nedeniyle. 
Alice'in e-postayı önce kendi posta sunucusuna bırakmasını sağlayarak, Alice'in posta sunucusu Bob'un posta sunucusu çalışır hale gelene kadar mesajı Bob'un posta sunucusuna göndermeyi tekrar tekrar deneyebilir, örneğin her 30 dakikada bir. (Ve eğer Alice'in posta sunucusu kapalıysa, o zaman sistem yöneticisine (**system administrator**) şikayet etme imkanı vardır!)

Ama yapbozun hala eksik bir parçası var! Bob gibi, yerel ana bilgisayarında bir kullanıcı ajanı çalıştıran bir alıcı, posta sunucusunda duran mesajlarını nasıl alır? 
Bob'un kullanıcı ajanının mesajları almak için SMTP kullanamayacağını unutmayın, çünkü mesajları almak bir çekme işlemi (**pull operation**) iken, SMTP bir itme protokolüdür (**push protocol**).

Bugün, Bob'un bir posta sunucusundan e-postasını almasının iki yaygın yolu vardır. Eğer Bob Web tabanlı e-posta (**Web-based e-mail**) veya bir akıllı telefon uygulaması (**smartphone app**) (Gmail gibi) kullanıyorsa, kullanıcı ajanı Bob'un e-postasını almak için HTTP kullanacaktır. Bu durum, Bob'un posta sunucusunun bir HTTP arayüzüne (**HTTP interface**) ve ayrıca bir SMTP arayüzüne (**SMTP interface**) (Alice'in posta sunucusuyla iletişim kurmak için) sahip olmasını gerektirir. Tipik olarak Microsoft Outlook gibi posta istemcilerinde kullanılan alternatif yöntem ise RFC 3501'de tanımlanan İnternet Posta Erişim Protokolü (IMAP) (**Internet Mail Access Protocol (IMAP)**)'ni kullanmaktır. Hem HTTP hem de IMAP yaklaşımları, Bob'un posta sunucusunda tutulan klasörleri (**folders**) yönetmesine olanak tanır. 
Bob, oluşturduğu klasörlere mesajları taşıyabilir, mesajları silebilir (**delete messages**), mesajları önemli olarak işaretleyebilir (**mark messages as important**) vb.

## DNS—İnternet'in Dizin Hizmeti

Biz insanlar birçok şekilde tanımlanabiliriz. Örneğin, doğum belgelerimizde yazan adlarla tanımlanabiliriz. 
Sosyal güvenlik numaralarımızla tanımlanabiliriz. Sürücü belgesi numaralarımızla tanımlanabiliriz. 
Her biri insanları tanımlamak için kullanılabilse de, belirli bir bağlamda bir tanımlayıcı diğerinden daha uygun olabilir. 
Örneğin, IRS'deki bilgisayarlar (Amerika Birleşik Devletleri'nin o meşhur vergi toplama kurumu) doğum belgesindeki adlar yerine sabit uzunluklu sosyal güvenlik numaralarını kullanmayı tercih eder. Öte yandan, sıradan insanlar sosyal güvenlik numaraları yerine daha akılda kalıcı olan doğum belgesindeki adları tercih ederler. (Gerçekten de, "Merhaba. Adım 999-231-987-54. Eşimle tanışın, 999-231-987-55" dediğinizi hayal edebilir misiniz?)

Tıpkı insanların birçok şekilde tanımlanabildiği gibi, İnternet ana bilgisayarları (**Internet hosts**) da öyle. 
Bir ana bilgisayar için tanımlayıcılardan biri ana bilgisayar adıdır (**hostname**). www.facebook.com, www.google.com, sakarya.edu gibi ana bilgisayar adları akılda kalıcıdır ve bu nedenle insanlar tarafından takdir edilir. Ancak, ana bilgisayar adları, ana bilgisayarın İnternet içindeki konumu hakkında çok az (veya hiç) bilgi sağlar. (www.redberks.tr gibi ülke kodu .tr ile biten bir ana bilgisayar adı, ana bilgisayarın muhtemelen Türkiye'de olduğunu söyler, ancak daha fazla bir şey söylemez.) Ayrıca, ana bilgisayar adları değişken uzunluklu alfasayısal karakterlerden oluşabildiği için, yönlendiriciler (**routers**) tarafından işlenmesi zor olacaktır. Bu nedenlerle, ana bilgisayarlar aynı zamanda sözde IP adresleri (**IP addresses**) ile de tanımlanır.

Bir IP adresi dört bayttan (**bytes**) oluşur ve katı bir hiyerarşik yapıya (**hierarchical structure**) sahiptir. 
Bir IP adresi 121.7.106.83 gibi görünür, burada her nokta ondalık gösterimde 0'dan 255'e kadar ifade edilen baytlardan birini ayırır. 
Bir IP adresi hiyerarşiktir, çünkü adresi soldan sağa doğru taradığımızda, ana bilgisayarın İnternet'te (yani, ağlar ağında hangi ağ içinde) nerede bulunduğuna dair giderek daha spesifik bilgi elde ederiz. Benzer şekilde, bir posta adresini alttan üste doğru taradığımızda, alıcının nerede bulunduğuna dair giderek daha spesifik bilgi elde ederiz.

#### DNS Tarafından Sağlanan Hizmetler

Bir ana bilgisayarı (**host**) tanımlamanın iki yolu olduğunu az önce gördük—bir ana bilgisayar adı (**hostname**) ve bir IP adresi (**IP address**) ile. 
İnsanlar daha akılda kalıcı olan ana bilgisayar adı tanımlayıcısını tercih ederken, yönlendiriciler (**routers**) sabit uzunluklu, hiyerarşik yapılı IP adreslerini tercih eder. Bu tercihleri uzlaştırmak için, ana bilgisayar adlarını IP adreslerine çeviren bir dizin hizmetine (**directory service**) ihtiyacımız var. Bu, İnternet'in alan adı sisteminin (DNS) (**domain name system (DNS)**) ana görevidir. 
DNS, (1) bir DNS sunucuları (**DNS servers**) hiyerarşisinde uygulanan dağıtılmış bir veritabanı (**distributed database**) ve (2) ana bilgisayarların (**hosts**) dağıtılmış veritabanını sorgulamasına (**query**) olanak tanıyan bir uygulama katmanı protokolüdür (**application-layer protocol**). 
DNS sunucuları genellikle Berkeley Internet Name Domain (BIND) yazılımını [BIND 2020] çalıştıran UNIX makineleridir (**UNIX machines**). 
DNS protokolü UDP (**UDP**) üzerinde çalışır ve 53 numaralı portu (**port 53**) kullanır.

DNS, kullanıcı tarafından sağlanan ana bilgisayar adlarını IP adreslerine çevirmek için HTTP (**HTTP**) ve SMTP (**SMTP**) dahil olmak üzere diğer uygulama katmanı protokolleri tarafından yaygın olarak kullanılır. Örnek olarak, bir kullanıcının ana bilgisayarında çalışan bir tarayıcının (yani, bir HTTP istemcisinin) www.redberks.com/index.html URL'sini istediğinde ne olduğunu düşünelim. Kullanıcının ana bilgisayarının Web sunucusu (**Web server**) www.redberks.com'a bir HTTP istek mesajı (**HTTP request message**) gönderebilmesi için, kullanıcının ana bilgisayarı önce www.redberks.com'un IP adresini almalıdır. 

Bu şu şekilde yapılır:

1. Aynı kullanıcı makinesi, DNS uygulamasının istemci tarafını çalıştırır.
2. Tarayıcı, URL'den ana bilgisayar adını (www.redberks.com) çıkarır ve ana bilgisayar adını DNS uygulamasının istemci tarafına iletir.
3. DNS istemcisi (**DNS client**), ana bilgisayar adını içeren bir sorguyu bir DNS sunucusuna (**DNS server**) gönderir.
4. DNS istemcisi sonunda, ana bilgisayar adının IP adresini içeren bir yanıt alır.
5. Tarayıcı DNS'ten IP adresini aldıktan sonra, o IP adresindeki 80 numaralı portta bulunan HTTP sunucu sürecine bir TCP bağlantısı başlatabilir.

Bu örnekten görüyoruz ki DNS, kendisini kullanan İnternet uygulamalarına ek bir gecikme—bazen önemli bir gecikme—ekler. Neyse ki, aşağıda tartışacağımız gibi, istenen IP adresi genellikle "yakın" bir DNS sunucusunda önbelleğe alınır, bu da DNS ağ trafiğini (**DNS network traffic**) ve ortalama DNS gecikmesini (**DNS delay**) azaltmaya yardımcı olur.

DNS, ana bilgisayar adlarını IP adreslerine çevirmenin yanı sıra birkaç önemli hizmet daha sağlar:

* **Ana Bilgisayar Takma Adı (Host aliasing).** Karmaşık bir ana bilgisayar adına sahip bir ana bilgisayar, bir veya daha fazla takma ada (**alias names**) sahip olabilir. Örneğin, relay1.west-coast.enterprise.com gibi bir ana bilgisayar adı, enterprise.com ve www.enterprise.com gibi iki takma ada sahip olabilir.
Bu durumda, relay1.west-coast.enterprise.com ana bilgisayar adının kurallı ana bilgisayar adı (**canonical hostname**) olduğu söylenir. Takma ad ana bilgisayar adları (**alias hostnames**), mevcut olduğunda, genellikle kurallı ana bilgisayar adlarından daha akılda kalıcıdır. DNS, sağlanan bir takma ad ana bilgisayar adı için kurallı ana bilgisayar adını ve ayrıca ana bilgisayarın IP adresini almak için bir uygulama tarafından çağrılabilir.

* **Posta Sunucusu Takma Adı (Mail server aliasing).** Açık nedenlerle, e-posta adreslerinin akılda kalıcı olması son derece arzu edilir. Örneğin, Bob'un Yahoo Mail'de bir hesabı varsa, Bob'un e-posta adresi bob@yahoo.com kadar basit olabilir. Ancak, Yahoo posta sunucusunun ana bilgisayar adı, yahoo.com'dan daha karmaşıktır ve çok daha az akılda kalıcıdır (örneğin, kurallı ana bilgisayar adı relay1.west-coast.yahoo.com gibi bir şey olabilir). DNS, sağlanan bir takma ad ana bilgisayar adı için kurallı ana bilgisayar adını ve ayrıca ana bilgisayarın IP adresini almak için bir posta uygulaması tarafından çağrılabilir. Aslında, MX kaydı (**MX record**) (aşağıya bakın), bir şirketin posta sunucusunun (**mail server**) ve Web sunucusunun (**Web server**) aynı (takma adlı) ana bilgisayar adlarına sahip olmasına izin verir; örneğin, bir şirketin Web sunucusu ve posta sunucusu her ikisi de enterprise.com olarak adlandırılabilir.
  
* **Yük Dağılımı (Load distribution).** DNS, çoğaltılmış sunucular (**replicated servers**), örneğin çoğaltılmış Web sunucuları arasında yük dağılımı yapmak için de kullanılır. cnn.com gibi yoğun siteler, her sunucunun farklı bir uç sistemde (**end system**) çalıştığı ve her birinin farklı bir IP adresine sahip olduğu birden fazla sunucu üzerinde çoğaltılır. Çoğaltılmış Web sunucuları için, bir grup IP adresi bu nedenle bir takma ad ana bilgisayar adıyla ilişkilendirilir.

PRATİK: DNS: İstemci-Sunucu Paradigması Aracılığıyla Kritik Ağ İşlevleri

HTTP, FTP ve SMTP gibi, DNS protokolü de bir uygulama katmanı protokolüdür, çünkü (1) istemci-sunucu paradigması (**client-server paradigm**) kullanarak iletişim kuran uç sistemler arasında çalışır ve (2) iletişim kuran uç sistemler arasında DNS mesajlarını (**DNS messages**) aktarmak için temel bir uçtan uca taşıma protokolüne (**end-to-end transport protocol**) dayanır. Ancak başka bir anlamda, DNS'in rolü Web, dosya transferi ve e-posta uygulamalarından oldukça farklıdır. Bu uygulamaların aksine, DNS, kullanıcının doğrudan etkileşimde bulunduğu bir uygulama değildir. 
Bunun yerine, DNS, İnternet'teki kullanıcı uygulamaları ve diğer yazılımlar için temel bir İnternet işlevi—yani, ana bilgisayar adlarını altındaki IP adreslerine çevirmeyi—sağlar (**network-name to network-address translation**). İnternet mimarisindeki karmaşıklığın çoğunun ağın "kenarlarında" (**edges**) bulunduğunu belirtmiştik. Kritik ad-adres çeviri işlemini (**name-to-address translation process**), ağın kenarında bulunan istemciler ve sunucular kullanarak uygulayan DNS, bu tasarım felsefesinin bir başka örneğidir. 

DNS veritabanı bu IP adresi kümesini içerir. İstemciler bir adres kümesine eşlenen bir ad için bir DNS sorgusu yaptığında, sunucu IP adreslerinin tamamını içeren bir yanıt verir, ancak her yanıtta adreslerin sıralamasını döndürür. Bir istemci tipik olarak HTTP istek mesajını kümede ilk sırada listelenen IP adresine gönderdiği için, DNS döndürmesi trafiği çoğaltılmış sunucular arasında dağıtır. DNS döndürmesi e-posta için de kullanılır, böylece birden fazla posta sunucusu aynı takma adı kullanabilir. Ayrıca, Akamai gibi içerik dağıtım şirketleri Web içerik dağıtımını sağlamak için DNS'i daha gelişmiş yollarla kullanmıştır [Dilley 2002] 

DNS, RFC 1034 ve RFC 1035'te belirtilmiştir ve birkaç ek RFC'de güncellenmiştir. 
Karmaşık bir sistemdir ve burada sadece temel yönlerine değiniyoruz. İlgilenen okuyucu bu RFC'lere ve Albitz ve Liu'nun kitabına [Albitz 1993] başvurabilir; ayrıca DNS'in ne olduğu ve nedenine dair güzel bir açıklama sunan geriye dönük makaleye [Mockapetris 1988] ve [Mockapetris 2005]'e de bakılabilir.

#### DNS Nasıl Çalışır?—Genel Bakış

Şimdi DNS'in nasıl çalıştığına dair üst düzey bir genel bakış sunacağız. 
Tartışmamız, ana bilgisayar adı-IP adresi çeviri hizmetine (**hostname-to-IP-address translation service**) odaklanacaktır.

Bir kullanıcının ana bilgisayarında (**user’s host**) çalışan bir uygulamanın (bir Web tarayıcısı veya bir posta istemcisi (**mail client**) gibi) bir ana bilgisayar adını (**hostname**) bir IP adresine çevirmesi gerektiğini varsayalım. 
Uygulama, çevrilmesi gereken ana bilgisayar adını belirterek DNS uygulamasının istemci tarafını çağıracaktır. (Birçok UNIX tabanlı makinede, uygulamanın çeviriyi gerçekleştirmek için çağırdığı fonksiyon çağrısı `gethostbyname()`'dir.) 
Daha sonra kullanıcının ana bilgisayarındaki DNS kontrolü ele alır ve ağa (**network**) bir sorgu mesajı (**query message**) gönderir. 
Tüm DNS sorgu ve yanıt mesajları, 53 numaralı porta (**port 53**) UDP datagramları (**UDP datagrams**) içinde gönderilir. 
Milisaniyelerden saniyelere kadar değişen bir gecikmeden sonra, kullanıcının ana bilgisayarındaki DNS, istenen eşlemeyi (**mapping**) sağlayan bir DNS yanıt mesajı (**DNS reply message**) alır. Bu eşleme daha sonra çağıran uygulamaya iletilir. Böylece, kullanıcının ana bilgisayarındaki çağıran uygulamanın bakış açısından, DNS basit, anlaşılır bir çeviri hizmeti sağlayan bir kara kutudur (**black box**). 
Ancak aslında, hizmeti uygulayan kara kutu karmaşıktır ve dünya çapında dağıtılmış çok sayıda DNS sunucusundan (**DNS servers**) ve DNS sunucularının ve sorgulayan ana bilgisayarların nasıl iletişim kurduğunu belirten bir uygulama katmanı protokolünden (**application-layer protocol**) oluşur.

DNS için basit bir tasarım, tüm eşlemeleri içeren tek bir DNS sunucusuna sahip olmaktı. 
Bu merkezileştirilmiş tasarımda (**centralized design**), istemciler tüm sorguları tek bir DNS sunucusuna yönlendirir ve DNS sunucusu sorgulayan istemcilere doğrudan yanıt verir. Bu tasarımın basitliği çekici olsa da, günümüzün İnternet'i için, devasa (ve büyüyen) ana bilgisayar sayısıyla, uygun değildir. 

Merkezileştirilmiş bir tasarımın sorunları şunlardır:

* **Tek bir hata noktası (A single point of failure).** DNS sunucusu çökerse, tüm İnternet de çöker!
* **Trafik hacmi (Traffic volume).** Tek bir DNS sunucusu, yüz milyonlarca ana bilgisayardan üretilen tüm HTTP istekleri (**HTTP requests**) ve e-posta mesajları (**e-mail messages**) için tüm DNS sorgularını yönetmek zorunda kalırdı.
* **Uzak merkezileştirilmiş veritabanı (Distant centralized database).** Tek bir DNS sunucusu, tüm sorgulayan istemcilere "yakın" olamaz. Eğer tek DNS sunucusunu New York şehrine koyarsak, Avustralya'dan gelen tüm sorguların dünyanın diğer ucuna, belki de yavaş ve yoğun bağlantılar üzerinden gitmesi gerekirdi. Bu önemli gecikmelere yol açabilir.
* **Bakım (Maintenance).** Tek DNS sunucusu, tüm İnternet ana bilgisayarlarının kayıtlarını tutmak zorunda kalırdı. Bu merkezileştirilmiş veritabanı devasa olmakla kalmaz, aynı zamanda her yeni ana bilgisayarı hesaba katmak için sık sık güncellenmesi gerekirdi.

Özetle, tek bir DNS sunucusundaki merkezileştirilmiş bir veritabanı ölçeklenemez (**scale**). Sonuç olarak, DNS tasarım gereği dağıtılmıştır (**distributed by design**). Aslında, DNS, dağıtılmış bir veritabanının İnternet'te nasıl uygulanabileceğinin harika bir örneğidir.

#### Dağıtılmış, Hiyerarşik Bir Veritabanı

Ölçek sorununu ele almak için, DNS, hiyerarşik bir şekilde düzenlenmiş ve dünya çapında dağıtılmış çok sayıda sunucu kullanır. 
Tek bir DNS sunucusu, İnternet'teki tüm ana bilgisayarların tüm eşlemelerini barındırmaz. 
Bunun yerine, eşlemeler DNS sunucuları arasında dağıtılır. 
İlk yaklaşıma göre, hiyerarşik olarak organize edilmiş üç sınıf DNS sunucusu vardır: kök DNS sunucuları (**root DNS servers**), üst düzey alan adı (TLD) DNS sunucuları (**top-level domain (TLD) DNS servers**) ve yetkili DNS sunucuları (**authoritative DNS servers**).

Bu üç sunucu sınıfının nasıl etkileşimde bulunduğunu anlamak için, bir DNS istemcisinin (**DNS client**) www.amazon.com ana bilgisayar adının IP adresini (**IP address**) belirlemek istediğini varsayalım. İlk yaklaşıma göre, aşağıdaki olaylar gerçekleşecektir. 
İstemci ilk olarak kök sunuculardan (**root servers**) biriyle iletişim kurar, bu sunucu .com üst düzey alanı için TLD sunucularının IP adreslerini döndürür. İstemci daha sonra bu TLD sunucularından biriyle iletişim kurar, bu sunucu amazon.com için yetkili bir sunucunun IP adresini döndürür. 
Son olarak, istemci amazon.com için yetkili sunuculardan biriyle iletişim kurar, bu sunucu www.amazon.com ana bilgisayar adı (**hostname**) için IP adresini döndürür. Bu DNS arama sürecini (**DNS lookup process**) yakında daha ayrıntılı inceleyeceğiz. Ama önce bu üç sınıf DNS sunucusuna daha yakından bakalım:

* **Kök DNS sunucuları.** Dünya çapında dağılmış 1000'den fazla kök sunucu örneği vardır.
Bu kök sunucular, 12 farklı kuruluş tarafından yönetilen ve İnternet Tahsisli Numaralar Otoritesi [IANA 2020] aracılığıyla koordine edilen 13 farklı kök sunucunun kopyalarıdır. Kök ad sunucularının tam listesi, onları yöneten kuruluşlar ve IP adresleri [https://www.iana.org/domains/root/servers]'da bulunabilir.
Kök ad sunucuları, TLD sunucularının IP adreslerini sağlar.

* **Üst düzey alan adı (TLD) sunucuları.** Üst düzey alan adlarının her biri için—com, org, net, edu ve gov gibi üst düzey alan adları ve uk, fr, ca ve jp gibi tüm ülke üst düzey alan adları için—bir TLD sunucusu (veya sunucu kümesi) bulunur. Verisign Global Registry Services şirketi, com üst düzey alanı için TLD sunucularını, Educause şirketi ise edu üst düzey alanı için TLD sunucularını yönetir. Bir TLD'yi destekleyen ağ altyapısı büyük ve karmaşık olabilir; Verisign ağına güzel bir genel bakış için [Osterweil 2012]'ye bakın. Tüm üst düzey alan adlarının listesi için [https://tld-list.com/]'ye bakın.
TLD sunucuları, yetkili DNS sunucularının IP adreslerini sağlar.
  
* **Yetkili DNS sunucuları.** İnternet üzerinde halka açık ana bilgisayarlara (**publicly accessible hosts**) (Web sunucuları ve posta sunucuları gibi) sahip her kuruluş, bu ana bilgisayarların adlarını IP adreslerine eşleyen halka açık DNS kayıtları (**DNS records**) sağlamalıdır. Bir kuruluşun yetkili DNS sunucusu, bu DNS kayıtlarını barındırır. Bir kuruluş bu kayıtları tutmak için kendi yetkili DNS sunucusunu kurmayı seçebilir; alternatif olarak, kuruluş bu kayıtların barındırılması için ödeme yapabilir.

Kök, TLD ve yetkili DNS sunucularının tümü, DNS sunucularının hiyerarşisine aittir. Yerel DNS sunucusu (**local DNS server**) adı verilen başka bir önemli DNS sunucusu türü vardır. Yerel DNS sunucusu, sunucu hiyerarşisine sıkı sıkıya ait değildir ancak yine de DNS mimarisi için merkezidir. 
Her İSS—bir konut İSS'si (**residential ISP**) veya kurumsal bir İSS (**institutional ISP**) gibi—bir yerel DNS sunucusuna (varsayılan ad sunucusu (**default name server**) olarak da adlandırılır) sahiptir. Bir ana bilgisayar bir İSS'ye bağlandığında, İSS ana bilgisayara bir veya daha fazla yerel DNS sunucusunun IP adresini sağlar. Windows veya UNIX'teki ağ durumu(network status) pencerelerine erişerek yerel DNS sunucunuzun IP adresini kolayca belirleyebilirsiniz. 
Bir ana bilgisayarın yerel DNS sunucusu tipik olarak ana bilgisayara "yakındır". Kurumsal bir İSS için, yerel DNS sunucusu ana bilgisayarla aynı LAN'da olabilir; konut İSS'si için, ana bilgisayardan genellikle birkaç yönlendiriciden daha fazla ayrılmamıştır. 
Bir ana bilgisayar DNS sorgusu yaptığında, sorgu yerel DNS sunucusuna gönderilir; bu sunucu bir proxy (**proxy**) gibi davranır ve sorguyu aşağıda daha ayrıntılı tartışacağımız DNS sunucu hiyerarşisine iletir.

Basit bir örneğe bakalım. cse.nyu.edu ana bilgisayarının gaia.cs.umass.edu'nun IP adresini istediğini varsayalım. Ayrıca NYU'nun cse.nyu.edu için yerel DNS sunucusunun dns.nyu.edu ve gaia.cs.umass.edu için yetkili bir DNS sunucusunun dns.umass.edu olarak adlandırıldığını varsayalım. cse.nyu.edu ana bilgisayarı ilk olarak yerel DNS sunucusuna, dns.nyu.edu'ya bir DNS sorgu mesajı (**DNS query message**) gönderir. 
Sorgu mesajı çevrilecek ana bilgisayar adını, yani gaia.cs.umass.edu'yu içerir. Yerel DNS sunucusu sorgu mesajını bir kök DNS sunucusuna iletir. 
Kök DNS sunucusu .edu son ekini not alır ve yerel DNS sunucusuna .edu'dan sorumlu TLD sunucularının IP adreslerinin bir listesini döndürür. 
Yerel DNS sunucusu daha sonra sorgu mesajını bu TLD sunucularından birine yeniden gönderir. TLD sunucusu umass.edu son ekini not alır ve Massachusetts Üniversitesi için yetkili DNS sunucusunun, yani dns.umass.edu'nun IP adresiyle yanıt verir. Son olarak, yerel DNS sunucusu sorgu mesajını doğrudan dns.umass.edu'ya yeniden gönderir, bu da gaia.cs.umass.edu'nun IP adresiyle yanıt verir. Bu örnekte, bir ana bilgisayar adı için eşlemeyi elde etmek amacıyla sekiz DNS mesajı gönderildiğine dikkat edin: dört sorgu mesajı ve dört yanıt mesajı! DNS önbelleklemenin bu sorgu trafiğini (**query traffic**) nasıl azalttığını yakında göreceğiz.

Önceki örneğimizde, TLD sunucusunun ana bilgisayar adı için yetkili DNS sunucusunu bildiği varsayıldı. 
Genel olarak, bu her zaman doğru değildir. Bunun yerine, TLD sunucusu yalnızca ara bir DNS sunucusunu biliyor olabilir ve bu sunucu da ana bilgisayar adı için yetkili DNS sunucusunu biliyor olabilir. Örneğin, Massachusetts Üniversitesi'nin üniversite için dns.umass.edu adlı bir DNS sunucusu olduğunu tekrar varsayalım. Ayrıca Massachusetts Üniversitesi'ndeki her bölümün kendi DNS sunucusuna sahip olduğunu ve her bölüm DNS sunucusunun bölümdeki tüm ana bilgisayarlar için yetkili olduğunu varsayalım. Bu durumda, ara DNS sunucusu, dns.umass.edu, cs.umass.edu ile biten bir ana bilgisayar adına sahip bir ana bilgisayar için bir sorgu aldığında, dns.cs.umass.edu'nun IP adresini dns.nyu.edu'ya döndürür; bu sunucu cs.umass.edu ile biten tüm ana bilgisayar adları için yetkilidir. 
Yerel DNS sunucusu dns.nyu.edu daha sonra sorguyu yetkili DNS sunucusuna gönderir, bu sunucu istenen eşlemeyi yerel DNS sunucusuna döndürür ve bu sunucu da eşlemeyi istekte bulunan ana bilgisayara geri döndürür. Bu durumda, toplam 10 DNS mesajı gönderilir!

cse.nyu.edu'dan dns.nyu.edu'ya gönderilen sorgu, dns.nyu.edu'dan eşlemeyi kendi adına almasını istediği için yinelemeli bir sorgudur. 
Ancak, sonraki üç sorgu tekrarlamalıdır, çünkü tüm yanıtlar doğrudan dns.nyu.edu'ya döndürülür. 
Teorik olarak, herhangi bir DNS sorgusu yinelemeli veya tekrarlamalı olabilir. 
Pratikte, sorgular tipik olarak şu kalıbı izler: İstek yapan ana bilgisayardan yerel DNS sunucusuna yapılan sorgu yinelemelidir ve kalan sorgular tekrarlamalıdır.

#### DNS Önbellekleme (Caching)

Şimdiye kadarki tartışmamız, DNS sisteminin kritik derecede önemli bir özelliği olan DNS önbelleklemesini (**DNS caching**) göz ardı etti. 
Gerçekte, DNS, gecikme performansını iyileştirmek ve İnternet etrafında sekerek dolaşan DNS mesajlarının sayısını azaltmak için DNS önbelleklemesini kapsamlı bir şekilde kullanır. DNS önbelleklemesinin ardındaki fikir çok basittir. 
Bir sorgu zincirinde, bir DNS sunucusu bir DNS yanıtı (**DNS reply**) (örneğin, bir ana bilgisayar adından (**hostname**) bir IP adresine (**IP address**) eşleme içeren) aldığında, eşlemeyi yerel belleğinde (**local memory**) önbelleğe alabilir. Örneğin, yerel DNS sunucusu dns.nyu.edu'nun bir DNS sunucusundan bir yanıt aldığı her seferde, yanıtta yer alan herhangi bir bilgiyi önbelleğe alabilir. Bir ana bilgisayar adı/IP adresi çifti bir DNS sunucusunda önbelleğe alınmışsa ve aynı ana bilgisayar adı için DNS sunucusuna başka bir sorgu gelirse, DNS sunucusu ana bilgisayar adı için yetkili olmasa bile istenen IP adresini sağlayabilir. Ana bilgisayarlar ve ana bilgisayar adları ile IP adresleri arasındaki eşlemeler kalıcı olmaktan uzak olduğu için, DNS sunucuları önbelleğe alınmış bilgileri belirli bir süre sonra (genellikle iki gün olarak ayarlanır) atar.

Örnek olarak, apricot.nyu.edu ana bilgisayarının redberks.com ana bilgisayar adı için IP adresini dns.nyu.edu'ya sorduğunu varsayalım. 
Ayrıca, birkaç saat sonra, başka bir NYU ana bilgisayarının, örneğin kiwi.nyu.edu'nun, aynı ana bilgisayar adıyla dns.nyu.edu'ya da sorduğunu varsayalım. Önbellekleme sayesinde, yerel DNS sunucusu (**local DNS server**), başka hiçbir DNS sunucusunu sorgulamak zorunda kalmadan redberks.com'un IP adresini bu ikinci istek yapan ana bilgisayara hemen döndürebilecektir. Yerel bir DNS sunucusu, TLD sunucularının (**TLD servers**) IP adreslerini de önbelleğe alabilir, bu da yerel DNS sunucusunun bir sorgu zincirindeki kök DNS sunucularını (**root DNS servers**) atlamasına olanak tanır. 
Aslında, önbellekleme sayesinde, DNS sorgularının çok küçük bir kısmı hariç tümü için kök sunucular atlanır.

#### DNS Kayıtları ve Mesajları

DNS dağıtılmış veritabanını (**DNS distributed database**) birlikte uygulayan DNS sunucuları (**DNS servers**), ana bilgisayar adı-IP adresi eşlemeleri (**hostname-to-IP address mappings**) sağlayan Kaynak Kayıtları (RR'ler) (**resource records (RRs)**) depolar. 
Her DNS yanıt mesajı (**DNS reply message**) bir veya daha fazla kaynak kaydı taşır. Bu ve sonraki alt bölümde, DNS kaynak kayıtlarına ve mesajlarına kısa bir genel bakış sunuyoruz; daha fazla ayrıntı [Albitz 1993]'te veya DNS RFC'lerinde [RFC 1034; RFC 1035] bulunabilir. 

Bir kaynak kaydı (**resource record**), aşağıdaki alanları içeren dört elemanlı bir dizidir (**four-tuple**):

(Name, Value, Type, TTL)

TTL (**time to live**), kaynak kaydının yaşam süresidir; bir kaynağın önbellekten ne zaman kaldırılması gerektiğini belirler. Aşağıdaki örnek kayıtlarda, TTL alanını dikkate almıyoruz. Name ve Value'nun anlamı Type'a bağlıdır:

* Eğer Type=A ise, Name bir ana bilgisayar adıdır (**hostname**) ve Value, ana bilgisayar adı için IP adresidir (**IP address**). Böylece, Type A kaydı (**Type A record**) standart ana bilgisayar adı-IP adresi eşlemesini (**standard hostname-to-IP address mapping**) sağlar. Örnek olarak, `(redberks.com, 141.37.93.146, A)` bir Type A kaydıdır.
* Eğer Type=NS ise, Name bir alandır (**domain**) (redberks.com gibi) ve Value, alan adındaki ana bilgisayarların IP adreslerinin nasıl elde edileceğini bilen yetkili bir DNS sunucusunun (**authoritative DNS server**) ana bilgisayar adıdır (**hostname**). Bu kayıt, DNS sorgularını sorgu zincirinde daha ileriye yönlendirmek için kullanılır. Örnek olarak, `(redberks.com, dns.redberks.com, NS)` bir Type NS kaydıdır (**Type NS record**).
* Eğer Type=CNAME ise, Value, Name takma ad ana bilgisayar adı (**alias hostname**) için kurallı ana bilgisayar adıdır (**canonical hostname**). Bu kayıt, sorgu yapan ana bilgisayarlara bir ana bilgisayar adı için kurallı adı sağlayabilir. Örnek olarak, `(redberks.com, relay1.test.redberks.com, CNAME)` bir CNAME kaydıdır (**Type CNAME record**).
* Eğer Type=MX ise, Value, Name takma ad ana bilgisayar adına sahip bir posta sunucusunun (**mail server**) kurallı adıdır (**canonical name**). Örnek olarak, `(redberks.com, mail.test.redberks.com, MX)` bir MX kaydıdır (**Type MX record**). MX kayıtları (**MX records**), posta sunucularının ana bilgisayar adlarının basit takma adlara sahip olmasına olanak tanır. MX kaydını kullanarak, bir şirketin posta sunucusu ve diğer sunucularından biri (Web sunucusu gibi) için aynı takma adı kullanabileceğine dikkat edin. Posta sunucusunun kurallı adını almak için, bir DNS istemcisi (**DNS client**) bir MX kaydı için sorgu yapacaktır; diğer sunucunun kurallı adını almak için ise DNS istemcisi CNAME kaydı (**CNAME record**) için sorgu yapacaktır.

Eğer bir DNS sunucusu (**DNS server**) belirli bir ana bilgisayar adı için yetkiliyse (**authoritative**), o zaman DNS sunucusu ana bilgisayar adı için bir Type A kaydı içerecektir. (Sunucu yetkili olmasa bile, önbelleğinde bir Type A kaydı içerebilir.) Eğer bir sunucu bir ana bilgisayar adı için yetkili değilse, o zaman sunucu, ana bilgisayar adını içeren alan adı (**domain**) için bir Type NS kaydı içerecektir; ayrıca Type NS kaydının Value alanında DNS sunucusunun IP adresini sağlayan bir Type A kaydı içerecektir. Örnek olarak, bir edu TLD sunucusunun redberks.edu ana bilgisayarı için yetkili olmadığını varsayalım. O zaman bu sunucu, redberks.edu ana bilgisayarını içeren bir alan adı için, örneğin `(redberks.edu, dns.redberks.edu, NS)` şeklinde bir kayıt içerecektir. edu TLD sunucusu ayrıca DNS sunucusu dns.redberks.edu'yu bir IP adresine eşleyen bir Type A kaydı da içerecektir, örneğin `(dns.redberks.edu, 128.119.40.111, A)`.

