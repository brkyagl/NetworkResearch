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
