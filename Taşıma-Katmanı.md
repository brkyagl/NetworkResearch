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

