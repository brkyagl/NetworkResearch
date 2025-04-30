# Taşıma Katmanı (Transport Layer)

Taşıma katmanı (**Transport Layer**), uygulamanın ve ağ katmanlarının (**application and network layers**) tam ortasında durur ve katmanlı ağ yapısının (**layered network architecture**) kilit oyuncusudur. En önemli görevi (**critical role**), farklı bilgisayarlarda (**hosts**) çalışan uygulama süreçlerine (**application processes**) doğrudan iletişim hizmetleri (**communication services**) sunmaktır.

Bu bölümde ilerlerken, bir yandan taşıma katmanının temel prensiplerini (**transport-layer principles**) konuşacağız, bir yandan da bu prensiplerin günlük hayatta kullandığımız protokollerde (**existing protocols**) nasıl işlediğini göreceğiz. 
Alıştığımız gibi, İnternet'in popüler protokollerine (**Internet protocols**) odaklanacağız, özellikle de iki büyük taşıma katmanı protokolü olan TCP ve UDP'ye (**TCP and UDP transport-layer protocols**).

İlk olarak, taşıma ve ağ katmanları (**transport and network layers**) arasındaki ilişkiye bakacağız. 
Bu, taşıma katmanının ilk hayati görevini (**critical function**) anlamamıza yardımcı olacak: ağ katmanının iki uç cihaz (**end systems**) arasındaki basit veri iletimini (**delivery service**), o cihazlardaki uygulamaların birbiriyle tam anlamıyla "konuşabileceği" bir hizmete dönüştürmek. 
İnternet'in 'bağlantısız' diye bilinen taşıma protokolü UDP (**connectionless transport protocol, UDP**) ile bu işlevi örneklendireceğiz.

Sonra tekrar temel prensiplere (**principles**) dönecek ve ağ oluşturmanın (**computer networking**) en can alıcı problemlerinden biriyle karşılaşacağız: 
Veriyi kaybedebilen (**lose data**) ve hatta bozabilen (**corrupt data**) bir ortamda, iki tarafın nasıl **güvenilir** bir şekilde iletişim kurabileceği (**communicate reliably**). Gittikçe daha karmaşık ama bir o kadar da gerçekçi senaryolar üzerinden, taşıma protokollerinin (**transport protocols**) bu 'güvenilir teslimat' sorununu çözmek için geliştirdiği birbirinden farklı teknikleri (**techniques**) adım adım inceleyeceğiz. 
Ardından, bu prensiplerin İnternet'in 'bağlantı yönelimli' taşıma protokolü TCP'de (**connection-oriented transport protocol, TCP**) nasıl hayat bulduğunu göreceğiz.

Ardından, ağ oluşturmanın (**networking**) ikinci büyük ve temel problemine geçeceğiz: Ağda **tıkanıklık (congestion)** yaşanmasını önlemek (**avoid**) veya tıkanıklık olduğunda durumu toparlamak (**recover from**) için, veri gönderen tarafların (**transport-layer entities**) gönderim hızlarını (**transmission rate**) nasıl ayarladıkları. Tıkanıklığın neden çıktığını, nelere sebep olduğunu (**causes and consequences of congestion**) ve bu iş için en çok kullanılan kontrol tekniklerini (**congestion-control techniques**) ele alacağız. Tıkanıklık kontrolünün arkasındaki meseleleri derinlemesine anladıktan sonra, TCP'nin bu karmaşık problemi nasıl ele aldığına (**TCP’s approach to congestion control**) odaklanacağız.

## Giriş ve Taşıma Katmanı Hizmetleri (Introduction and Transport-Layer Services)

Taşıma katmanı hakkında zaten öğrendiklerimizi hızlıca gözden geçirelim.

Bir taşıma katmanı protokolü (**transport-layer protocol**), farklı ana bilgisayarlarda (**hosts**) çalışan uygulama süreçleri (**application processes**) arasında mantıksal iletişim (**logical communication**) sağlar. 
Mantıksal iletişim ile kastettiğimiz şudur: Bir uygulamanın bakış açısından (**application’s perspective**), süreçleri çalıştıran ana bilgisayarlar sanki doğrudan birbirine bağlıymış (**directly connected**) gibidir; gerçekte ise, ana bilgisayarlar dünyanın farklı uçlarında olabilir, çok sayıda yönlendirici (**routers**) ve geniş bir yelpazedeki bağlantı türleri (**link types**) aracılığıyla birbirine bağlı olabilirler. 
Uygulama süreçleri, mesajları (**messages**) taşımak için kullanılan fiziksel altyapının (**physical infrastructure**) detayları hakkında endişelenmeden, taşıma katmanı tarafından sağlanan mantıksal iletişimi kullanarak birbirlerine mesaj gönderirler.

Taşıma katmanı protokolleri ağ yönlendiricilerinde (**network routers**) değil, **uç sistemlerde** (**implemented in the end systems**) uygulanır. 
Gönderen tarafta (**sending side**), taşıma katmanı, gönderen bir uygulama sürecinden (**sending application process**) aldığı uygulama katmanı mesajlarını (**application-layer messages**), İnternet terminolojisinde taşıma katmanı segmentleri (**transport-layer segments**) olarak bilinen taşıma katmanı paketlerine (**transport-layer packets**) dönüştürür. Bu, (muhtemelen) uygulama mesajlarını daha küçük parçalara ayırarak (**breaking the application messages into smaller chunks**) ve her parçaya bir taşıma katmanı başlığı (**transport-layer header**) ekleyerek taşıma katmanı segmentini oluşturmak suretiyle yapılır. 
Taşıma katmanı daha sonra segmenti gönderen uç sistemdeki ağ katmanına (**network layer at the sending end system**) iletir, burada segment bir ağ katmanı paketi (**network-layer packet**) (bir datagram - **datagram**) içine kapsüllenir (**encapsulated**) ve hedefe (**destination**) gönderilir. 
Ağ yönlendiricilerinin sadece datagramın ağ katmanı alanlarına (**network-layer fields**) etki ettiğini; yani, datagram içine kapsüllenmiş taşıma katmanı segmentinin alanlarını incelemediklerini (**examine the fields**) unutmamak önemlidir. 
Alan tarafta (**receiving side**), ağ katmanı taşıma katmanı segmentini datagramdan çıkarır (**extracts the transport-layer segment**) ve segmenti taşıma katmanına yukarı doğru iletir (**passes the segment up to the transport layer**). Taşıma katmanı daha sonra alınan segmenti işler (**processes the received segment**) ve segmentteki veriyi (**data**) alıcı uygulamaya (**receiving application**) kullanılabilir hale getirir.

Ağ uygulamaları için birden fazla taşıma katmanı protokolü mevcut olabilir. 
Örneğin, İnternet'in iki protokolü vardır—TCP ve UDP. Bu protokollerin her biri, çağıran uygulamaya (**invoking application**) farklı bir dizi taşıma katmanı hizmeti (**different set of transport-layer services**) sunar.

### Taşıma Katmanı ve Ağ Katmanları Arasındaki İlişki

Protokol yığınında taşıma katmanının ağ katmanının hemen üzerinde yer aldığını hatırlayalım. 
Ağ katmanı bilgisayarlar (host'lar) arasında mantıksal iletişim sağlarken, taşıma katmanı farklı bilgisayarlar üzerinde çalışan **süreçler** arasında mantıksal iletişim sağlar. Bu ayrım ince ama önemlidir. Gelin, bu farkı bir ev benzetmesiyle inceleyelim.

Doğu Yakası'nda bir evde ve Batı Yakası'nda başka bir evde oturan, her birinde on ikişer çocuğun yaşadığı iki ev düşünün. 
Doğu Yakası'ndaki evin çocukları, Batı Yakası'ndaki evin çocuklarının kuzenleri. 
İki evdeki çocuklar birbirlerine mektup yazmayı çok seviyorlar; her çocuk her hafta her kuzenine yazıyor ve her mektup geleneksel posta hizmetiyle ayrı bir zarfta teslim ediliyor. Böylece, her ev her hafta diğer eve 144 mektup gönderiyor. (Bu çocukların e-posta kullanıyor olsalardı çok para tasarrufu yapacakları kesin!) 
Her evde, posta toplama ve dağıtmadan sorumlu bir çocuk var: Batı Yakası'ndaki evde Ann ve Doğu Yakası'ndaki evde Bill. 
Ann her hafta tüm kardeşlerini ziyaret ediyor, postayı topluyor ve günlük olarak eve uğrayan posta hizmeti görevlisine veriyor. 
Mektuplar Batı Yakası'ndaki eve geldiğinde, Ann'in aynı zamanda postayı kardeşlerine dağıtma görevi de var. Bill'in de Doğu Yakası'nda benzer bir görevi var.

Bu örnekte, posta hizmeti iki ev arasında mantıksal iletişim sağlıyor—posta hizmeti postayı kişiden kişiye değil, evden eve taşıyor. 
Öte yandan, Ann ve Bill kuzenler arasında mantıksal iletişim sağlıyorlar—Ann ve Bill kardeşlerinden postayı alıp onlara postayı teslim ediyorlar. 
Şunu unutmayın ki, kuzenlerin bakış açısına göre, Ann ve Bill posta hizmetinin kendisi gibidir, oysa Ann ve Bill uçtan uca teslimat sürecinin sadece bir parçasıdır (uç sistem kısmı). Bu ev örneği, taşıma katmanının ağ katmanıyla nasıl ilişkili olduğunu açıklamak için güzel bir benzetme görevi görür:

* uygulama mesajları = zarf içindeki mektuplar
* süreçler = kuzenler
* hosts = evler
* taşıma katmanı protokolü = Ann ve Bill
* ağ katmanı protokolü = posta hizmeti (postacılar dahil)

Bu benzetmeyle devam edersek, Ann ve Bill'in tüm işlerini kendi evlerinde yaptıklarını unutmayın; örneğin, herhangi bir ara posta merkezinde postayı ayırma veya postayı bir posta merkezinden diğerine taşıma gibi işlemlere dahil değiller. Benzer şekilde, taşıma katmanı protokolleri uç sistemlerde yaşar. 
Bir uç sistem içinde, bir taşıma protokolü mesajları uygulama süreçlerinden ağın kenarına (yani ağ katmanına) taşır ve tam tersi; ancak mesajların ağ çekirdeği içinde nasıl taşınacağı hakkında söz hakkı yoktur. Nitekim, aradaki yönlendiriciler (router), taşıma katmanının uygulama mesajlarına eklemiş olabileceği herhangi bir bilgiyi ne kullanır ne de tanır.

Aile destanımızla devam edelim, şimdi varsayalım ki Ann ve Bill tatile çıktığında, başka bir kuzen çifti—diyelim Susan ve Harvey—onların yerine geçerek ev içi posta toplama ve dağıtımını sağlıyor. Ne yazık ki iki aile için, Susan ve Harvey toplama ve dağıtımı Ann ve Bill ile tamamen aynı şekilde yapmıyor. 
Daha küçük çocuklar oldukları için, Susan ve Harvey postayı daha az sıklıkla alıp bırakıyorlar ve zaman zaman mektupları kaybediyorlar (bazen aile köpeği tarafından çiğneniyorlar). Böylece, kuzen çifti Susan ve Harvey, Ann ve Bill ile aynı hizmet setini (yani aynı hizmet modelini) sağlamıyorlar. 
Benzer şekilde, bir bilgisayar ağı, her protokolün uygulamalara farklı bir hizmet modeli sunduğu birden fazla taşıma protokolünü kullanılabilir hale getirebilir.

Ann ve Bill'in sağlayabileceği olası hizmetler, posta hizmetinin sağlayabileceği olası hizmetlerle açıkça sınırlıdır. 
Örneğin, posta hizmeti iki ev arasında postayı teslim etmenin ne kadar süreceği konusunda (örneğin üç gün gibi) maksimum bir sınır koymuyorsa, Ann ve Bill'in herhangi bir kuzen çifti arasında posta teslimatı için maksimum bir gecikmeyi garanti etmesinin bir yolu yoktur. 
Benzer şekilde, bir taşıma protokolünün sağlayabileceği hizmetler genellikle alttaki ağ katmanı protokolünün hizmet modeli tarafından kısıtlanır. 
Eğer ağ katmanı protokolü bilgisayarlar arasında gönderilen taşıma katmanı segmentleri için gecikme veya bant genişliği garantisi sağlayamıyorsa, taşıma katmanı protokolü de süreçler arasında gönderilen uygulama mesajları için gecikme veya bant genişliği garantisi sağlayamaz.

Yine de, alttaki ağ protokolü ağ katmanında karşılık gelen hizmeti sunmasa bile, bir taşıma protokolü belirli hizmetleri sunabilir. 
Örneğin, bu bölümde göreceğimiz gibi, bir taşıma protokolü, alttaki ağ protokolü güvenilmez olsa bile, yani ağ protokolü paketleri kaybetse, bozsa veya çoğaltsa bile, uygulamaya güvenilir veri aktarımı hizmeti sunabilir. 
Başka bir örnek olarak, bir taşıma protokolü, ağ katmanı taşıma katmanı segmentlerinin gizliliğini garanti edemese bile, uygulama mesajlarının davetsiz misafirler tarafından okunmamasını garanti etmek için şifreleme kullanabilir.

### İnternet'teki Taşıma Katmanına Genel Bakış

İnternet'in uygulama katmanına iki farklı taşıma katmanı protokolü sunduğunu hatırlayalım. 
Bu protokollerden biri, çağıran uygulamaya **güvenilmez, bağlantısız bir hizmet** sağlayan **UDP** (User Datagram Protocol). 
İkinci protokol ise, çağıran uygulamaya **güvenilir, bağlantı yönelimli bir hizmet** sunan **TCP** (Transmission Control Protocol). 
Bir ağ uygulaması tasarlarken, uygulama geliştiricisinin bu iki taşıma protokolünden birini belirlemesi gerekir. 
Gördüğümüz gibi, uygulama geliştiricisi soketleri (socket) oluştururken UDP ve TCP arasında seçim yapar.

Terminolojiyi basitleştirmek için, taşıma katmanı paketine **segment** diyoruz. 
Ancak, İnternet literatüründe (örneğin RFC'lerde), TCP için taşıma katmanı paketine de segment denildiğini, ancak UDP paketi için genellikle **datagram** (datagram) denildiğini belirtmekte fayda var. Ne var ki, aynı İnternet literatürü, ağ katmanı paketi için de datagram terimini kullanır!
Bilgisayar ağları üzerine bu tür bir başlangıç için, hem TCP hem de UDP paketlerine segment demenin ve datagram terimini sadece ağ katmanı paketi (IP paketi) için saklamanın kafa karıştırıcı olmayacağını düşünüyoruz.

UDP ve TCP'ye kısa bir giriş yapmadan önce, İnternet'in ağ katmanı hakkında birkaç şey söylemek faydalı olacaktır. 
İnternet'in ağ katmanı protokolünün bir adı var: **IP** (Internet Protokolü). IP, bilgisayarlar (host'lar) arasında mantıksal iletişim sağlar. 
IP hizmet modeli, **en iyi çaba ile teslimat** (best-effort delivery) hizmetidir. 
Bu, IP'nin iletişim kuran bilgisayarlar arasında segmentleri teslim etmek için "en iyi çabayı" göstermesi anlamına gelir, ancak hiçbir **garanti** vermez. Özellikle, segment teslimatını garanti etmez, segmentlerin sıralı teslimatını garanti etmez ve segmentlerdeki verinin bütünlüğünü garanti etmez. 
Bu nedenlerle, IP **güvenilmez bir hizmet** olarak adlandırılır. 
Ayrıca burada belirtelim ki, her bilgisayarın en az bir ağ katmanı adresi, yani bir **IP adresi** vardır. 
IP adreslemeyi detaylı olarak inceleyeceğiz; bu bölüm için sadece her bilgisayarın bir IP adresi olduğunu aklımızda tutmamız yeterlidir.

IP hizmet modeline bir göz attığımıza göre, şimdi UDP ve TCP tarafından sağlanan hizmet modellerini özetleyelim. 
UDP ve TCP'nin en temel sorumluluğu, IP'nin iki uç sistem (end systems) arasındaki teslimat hizmetini, bu uç sistemlerde çalışan iki **süreç** arasındaki bir teslimat hizmetine genişletmektir. Bilgisayardan bilgisayara teslimatı süreçten sürece teslimata genişletme işlemine taşıma katmanı **çoklama (multiplexing)** ve **ayırma (demultiplexing)** denir. Taşıma katmanı çoklama ve ayırmayı bir sonraki bölümde tartışacağız. 
UDP ve TCP ayrıca, segment başlıklarındaki hata tespit alanlarını dahil ederek **bütünlük kontrolü** sağlarlar.

Bu iki minimal taşıma katmanı hizmeti—süreçten sürece veri teslimatı ve hata kontrolü—UDP'nin sağladığı **tek** iki hizmettir! 
Özellikle, IP gibi, UDP de **güvenilmez bir hizmettir**—bir süreç tarafından gönderilen verinin hedef sürece sağlam (veya hiç!) ulaşıp ulaşmayacağını garanti etmez. 

TCP ise, uygulamalara birkaç ek hizmet sunar. Her şeyden önce, **güvenilir veri aktarımı** (reliable data transfer) sağlar. 
**Akış kontrolü** (flow control), **sıra numaraları** (sequence numbers), **onaylar** (ACK'ler) ve **zamanlayıcılar** (timers) (bu bölümde detaylıca inceleyeceğimiz teknikler) kullanarak, TCP verinin gönderen süreçten alan sürece **doğru ve sıralı** bir şekilde teslim edilmesini sağlar. 
Böylece TCP, IP'nin uç sistemler arasındaki güvenilmez hizmetini, süreçler arasında güvenilir bir veri taşıma hizmetine dönüştürür. 
TCP ayrıca **tıkanıklık kontrolü** (congestion control) sağlar.
Tıkanıklık kontrolü, çağıran uygulamaya sağlanan bir hizmetten çok, bir bütün olarak İnternet için, yani genel fayda için bir hizmettir. 
Genel olarak konuşmak gerekirse, TCP tıkanıklık kontrolü, herhangi bir TCP bağlantısının, iletişim kuran bilgisayarlar arasındaki bağlantıları ve yönlendiricileri (router) aşırı miktarda trafikle boğmasını önler. TCP, tıkanık bir bağlantıdan geçen her bağlantıya, bağlantı **bant genişliğinden eşit pay** vermeye çalışır. 
Bu, TCP bağlantılarının gönderen taraflarının ağa trafik gönderme hızını (**transmission rate**) düzenleyerek yapılır.

UDP trafiği ise bunun tersine **düzenlenmemiş**tir. UDP taşıması kullanan bir uygulama, istediği hızda ve istediği süre boyunca veri gönderebilir.

Güvenilir veri aktarımı ve tıkanıklık kontrolü sağlayan bir protokol zorunlu olarak **karmaşık**tır. 
Güvenilir veri aktarımı prensiplerini ve tıkanıklık kontrolü prensiplerini ele almak için birkaç bölüme ve TCP protokolünün kendisini ele almak için ek bölümlere ihtiyacımız olacak. Bu bölümde benimsenen yaklaşım, temel prensipler ile TCP protokolü arasında geçiş yapmaktır. 
Örneğin, önce güvenilir veri aktarımını genel bir bağlamda tartışacağız ve ardından TCP'nin güvenilir veri aktarımını özel olarak nasıl sağladığını konuşacağız. Benzer şekilde, önce tıkanıklık kontrolünü genel bir bağlamda tartışacağız ve ardından TCP'nin tıkanıklık kontrolünü nasıl yaptığını ele alacağız.
Ama tüm bu güzel konulara girmeden önce, taşıma katmanı çoklama ve ayırmaya bir göz atalım.

## Çoklama (Multiplexing) ve Ayırma (Demultiplexing)

Bu bölümde, taşıma katmanının yaptığı temel bir işi konuşacağız: İnternet'ten bilgisayarına gelen veriyi, o bilgisayarda çalışan **doğru uygulamaya** (veya biz ona **süreç** diyelim) nasıl ulaştırdığı. Teknik dilde buna **çoklama (multiplexing)** ve **ayırma (demultiplexing)** deniyor. Merak etme, bunu o basit ev benzetmesiyle kolayca anlayacağız.

**Temel Problem Ne?**

Şöyle düşün: Senin bilgisayarın bir ev gibi. Bu evde aynı anda birçok çocuk (uygulama) yaşıyor: tarayıcı, oyun, sohbet programı gibi. 
İnternetten gelen veri paketleri de eve gelen mektuplar gibi. 
Problem şu: Eve gelen postanın (veri paketlerinin) hangi çocuğa (hangi uygulamaya) ait olduğunu nasıl bileceğiz? 
Posta kutusuna (internet bağlantına) gelen paketlerin doğru çocuğa gitmesi lazım.

**Çocukların Kapıları (Soketler) ve Kapı Numaraları (Portlar)**

İşte burada taşıma katmanı (bizim benzetmedeki postacı yardımcıları) devreye giriyor. 
Onlar şöyle bir sistem kurmuş:

1.  Evdeki her çocuk (her uygulama süreci), internetle konuşmak için kendine özel bir **kapı** açıyor. Bu kapılara teknik dilde **Soket (Socket)** deniyor.
2.  Bu kapıları karıştırmamak için, her kapıya benzersiz bir **numara** veriyorlar. Bu numaralara da **Port Numarası** deniyor. Yani, tarayıcı uygulamasının ayrı bir soketi ve port numarası var, oyunun ayrı, sohbet programının ayrı...

**Paket Gönderme (Çoklama / Multiplexing)**

Şimdi veri gönderme tarafına bakalım (İşte burası **Çoklama - Multiplexing** işi):

* Evdeki bir çocuk (uygulama süreci) bir mektup (veri) göndermek istiyor.
* Mektubu kendi kapısından (kendi özel port numarası olan soketinden) postacı yardımcısına (taşıma katmanı) veriyor.
* Postacı yardımcısı (taşıma katmanı), bu mektubu alıyor ve üzerine bir etiket yapıştırıyor. Bu etikette iki ana bilgi var:
    * **"Bu mektup hangi kapıdan çıktı?"** (Kaynak Port Numarası)
    * **"Bu mektup karşı evdeki hangi kapıya gidecek?"** (Hedef Port Numarası)
* Bu etiketlenmiş mektuba (yani başlığı eklenmiş veri parçasına) biz **segment** diyoruz (taşıma katmanı segmenti).
* Taşıma katmanı, farklı çocuklardan/kapılardan gelen bu segmentleri alıp, evin posta kutusuna (ağ katmanına) bırakıyor.
Ağ katmanı da bu segmentleri bir paket (datagram) içine koyup gerçek postacıyla (internet üzerinden) karşı eve gönderiyor.

**Paket Alma (Ayırma / Demultiplexing)**

Şimdi veri alma tarafına bakalım (İşte burası **Ayırma - Demultiplexing** işi):

* Gerçek postacı (ağ katmanı), internetten gelen bir paket (datagram) getirip evin posta kutusuna (bilgisayarın internet bağlantısına) bırakıyor.
* Evdeki postacı yardımcısı (taşıma katmanı) paketi alıyor ve içinden mektubu (segmenti) çıkarıyor.
* Segmentin üzerindeki etikete bakıyor ve özellikle **"Bu mektup hangi kapıya gidecek?"** (Hedef Port Numarası) yazan kısma odaklanıyor.
* Sonra evdeki o port numarasına (etikette yazan numaraya) sahip olan kapıyı (soketi) buluyor.
* Mektubun içindeki veriyi o kapıdan içeri atıyor. O kapıyı açmış bekleyen çocuk (uygulama süreci) da böylece kendi verisini almış oluyor.
* İşte taşıma katmanının, gelen paketleri alıp üzerindeki **hedef port numarasına** bakarak **doğru sokete** (dolayısıyla doğru sürece) teslim etme işine **Ayırma (Demultiplexing)** denir.

Taşıma katmanının ayırma (demultiplexing) hizmetini nasıl uygulayabileceği şimdi açık olmalıdır: Bilgisayardaki her sokete bir port numarası atanabilir ve bir segment bilgisayara ulaştığında, taşıma katmanı segmentteki hedef port numarasını inceler ve segmenti ilgili sokete yönlendirir. 
Segmentin verisi daha sonra soket aracılığıyla bağlı sürece geçer. Göreceğimiz gibi, UDP temelde bunu böyle yapar.
Ancak, TCP'deki çoklama/ayırmanın daha ince/karmaşık olduğunu da göreceğiz. 

**Özetle:**

- **Çoklama (Multiplexing):** Gönderme tarafında, farklı uygulamalardan/soketlerden gelen veriyi toplayıp, hangi soketten geldiğini ve kime gideceğini belirten etiketler (başlıklar) ekleyerek gönderme işi.
- **Ayırma (Demultiplexing):** Alma tarafında, gelen paketlerin üzerindeki etiketlere (başlıktaki hedef port numarasına) bakarak veriyi doğru uygulamaya/sokete teslim etme işi.

**Port Numaraları Hakkında Kısa Not:**

0'dan 1023'e kadar değişen port numaralarına **iyi bilinen port numaraları** (well-known port numbers) denir ve bunlar kısıtlanmıştır, yani HTTP (port numarası 80'i kullanır) ve FTP (port numarası 21'i kullanır) gibi iyi bilinen uygulama protokolleri tarafından kullanılmak üzere ayrılmıştır. İyi bilinen port numaralarının listesi RFC 1700'de verilmiştir ve http://www.iana.org adresinde güncellenmektedir [RFC 3232]. Yeni bir uygulama geliştirdiğimizde (geliştirdiğimiz basit uygulama gibi), uygulamaya bir port numarası atamalıyız.

#### Bağlantısız Çoklama ve Ayırma (UDP)

Önceki kısımlardan hatırlarsan, Python kodunda bir UDP soketi (socket) şöyle oluşturuluyordu:

```python
clientSocket = socket(AF_INET, SOCK_DGRAM)
```

Bu şekilde bir UDP soketi açtığında, taşıma katmanı (yani evdeki postacı yardımcısı) otomatik olarak bu sokete bir **Port Numarası** atar. 
Bu numarayı genellikle 1024 ile 65535 arasındaki bir aralıktan seçer ve o anda bilgisayarda (host) başka hiçbir UDP soketinin kullanmadığı bir numara verir. 
Ama istersek, soketi oluşturduktan sonra `bind()` metodunu kullanarak bu UDP soketine belirlediğimiz özel bir port numarasını da atayabiliriz:

```python
clientSocket.bind(('', 19157)) # Örneğin 19157 portunu atadık
```

Eğer bir server programı yazıyorsak ve bu server bilinen bir hizmet (Web server gibi) sunuyorsa, o zaman yazılımcı olarak server soketine o hizmetin iyi bilinen port numarasını (Web için 80 gibi) özellikle atamamız gerekir. 
Genellikle, Client tarafı port atamasını taşıma katmanına bırakır (otomatik ve gizlice yapar), Server tarafı ise belirli, sabit bir port numarası atar ki Client'lar onu bulabilsin.

**UDP Paketleri Nasıl Hazırlanır ve Nasıl Yönlendirilir? (Çoklama ve Ayırma)**

Artık UDP soketlerine port numaraları atandığına göre, UDP'nin çoklama (multiplexing) ve ayırma (demultiplexing) işini tam olarak nasıl yaptığını anlatalım:

Diyelim ki A Bilgisayarındaki (birinci evdeki) bir süreç (çocuk), 19157 numaralı kapıyı (UDP portunu) kullanarak B Bilgisayarındaki (karşı evdeki) 46428 numaralı kapısı olan bir sürece (çocuğa) bir parça uygulama verisi (mektup içi) göndermek istiyor.

* **A Bilgisayarında (Çoklama - Multiplexing):** A Bilgisayarındaki taşıma katmanı (birinci evdeki postacı yardımcısı), gönderilmek istenen veriyi (mektup içini) alır. Üzerine bir etiket yapıştırır. Bu etikette (taşıma katmanı başlığı - header) verinin kendisiyle birlikte şu bilgiler mutlaka bulunur:
    * **Kaynak Port Numarası:** 19157 (Mektup bizim evdeki hangi kapıdan çıktı?)
    * **Hedef Port Numarası:** 46428 (Karşı evdeki hangi kapıya gidecek?)
    * (Ve daha sonra konuşacağımız birkaç başka bilgi daha).
    Bu etiketlenmiş veriye biz **segment** diyoruz (taşıma katmanı segmenti). Taşıma katmanı bu segmenti alıp, evin posta kutusuna (ağ katmanına) verir.
    Ağ katmanı da segmenti bir IP datagramı (ağ katmanı paketi) içine koyar ve en iyi çabayla B Bilgisayarına ulaştırmaya çalışır.

* **B Bilgisayarında (Ayırma - Demultiplexing):** Eğer segment B Bilgisayarına (karşı eve) ulaşırsa, B Bilgisayarındaki taşıma katmanı (karşı evdeki postacı yardımcısı) paketi alır ve içinden segmenti çıkarır. Segmentin üzerindeki etikete (başına) bakar.

Segmenti hangi sokete (hangi kapıya) teslim edeceğini anlamak için **sadece** **Hedef Port Numarası**'na (46428) ve paketin geldiği **Hedef IP Adresi**'ne (kendi evin IP adresi) bakar.

**Çok Önemli Detay (UDP'nin Farkı):** 

Bir UDP soketini bilgisayar içinde bulmak (ayırma yapmak) için taşıma katmanı **sadece Hedef IP Adresi ve Hedef Port Numarası**'na bakar. 
Mektubun **Hangi Evden (Kaynak IP)** geldiğiyle veya **Hangi Kapıdan (Kaynak Port)** çıktığıyla **ilgilenmez**. 
Eğer iki farklı evden (farklı Kaynak IP) veya aynı evin farklı çocuklarından/kapılarından (farklı Kaynak Port) gelen iki segmentin **HEPSİNİN** üzerinde **AYNI Hedef IP Adresi** (karşı evin adresi) ve **AYNI Hedef Port Numarası** (karşı evdeki aynı kapı numarası) yazıyorsa, taşıma katmanı o iki segmenti de **AYNI Sokete** (yani aynı uygulama sürecine) teslim eder. 
Ağdan UDP segmentleri geldikçe, bilgisayar her segmenti ilgili sokete, segmentin hedef port numarasına bakarak yönlendirir (ayırma işlemini yapar).

**Kaynak Port Numarası Neden Var O Zaman?**

Madem ayırma sırasında kaynak portun önemi yok, neden var? **kaynak port numarası bir "dönüş adresinin" parçası olarak kullanılır.** 
B Bilgisayarı A Bilgisayarına bir yanıt (segment) göndermek istediğinde, B'den A'ya giden segmentteki **hedef port** değeri, A'dan B'ye giden segmentin **kaynak port** değerinden alınır. (Tam dönüş adresi, A'nın IP adresi ve A'dan gelen paketin kaynak port numarasıdır.)

Bu durum, incelediğimiz UDP server programında net görülüyordu. `UDPServer.py`'de server, gelen segmentten `recvfrom()` metodu ile client'ın kaynak port numarasını (ve IP adresini) çıkarıyordu. Sonra client'a geri gönderdiği yanıt segmentinde, bu çıkarılan kaynak port numarasını **hedef port** olarak kullanıyordu. İşte kaynak port numarası bu işe yarar: Karşı tarafın sana geri dönebilmesi için bir adres (port) bilgisi sağlamak.

#### Bağlantı Yönelimli Çoklama ve Ayırma (TCP)

Şimdi sıra TCP'de çoklama ve ayırma işinin nasıl yapıldığına geldi. TCP, UDP'den biraz farklı çalışır. 
TCP'deki en temel farklardan biri şudur: Bir TCP soketi (socket) (ve aslında kurulan TCP bağlantısı), UDP'deki gibi sadece hedef port numarasıyla değil, **dört farklı bilgiyle birden** tanımlanır. 

Biz buna **dörtlü** diyelim:

1.  **Kaynak IP Adresi:** Paketi gönderen bilgisayarın adresi (evin adresi gibi).
2.  **Kaynak Port Numarası:** Paketi gönderen bilgisayardaki sürecin (uygulamanın) açtığı kapının numarası.
3.  **Hedef IP Adresi:** Paketin gideceği bilgisayarın adresi (karşı evin adresi gibi).
4.  **Hedef Port Numarası:** Paketin gideceği bilgisayardaki sürecin (uygulamanın) kapısının numarası.

Yani, bir TCP segmenti (paketi) ağdan alıcı bilgisayara ulaştığında, bilgisayarın taşıma katmanı (postacı yardımcısı), segmenti **doğru sokete (doğru kapıya) yönlendirmek (ayırmak)** için **bu dört bilginin tamamını** kullanır.

**Bu Neden Önemli ve UDP'den Farkı Ne?**

İşte fark burada ortaya çıkıyor: UDP'de taşıma katmanı gelen paketi ayırırken sadece paketin üzerindeki "Hedef Port Numarası"na bakıyordu ve aynı hedef porta giden tüm paketler aynı sokete gidiyordu. Ama TCP'de durum farklı! 
TCP'de, farklı Kaynak IP adreslerinden veya farklı Kaynak Port numaralarından gelen iki segment (ilk bağlantı kurma isteği segmenti hariç), eğer **hedef IP adresi ve hedef port numarası aynı olsa bile**, **iki farklı sokete** yönlendirilir. 
Çünkü TCP, paketin hem kime (Hedef IP + Hedef Port) gittiğine hem de **kimden (Kaynak IP + Kaynak Port)** geldiğine bakar. 
Bu dört bilginin tamamı aynı olan paketler aynı sokete gider.

