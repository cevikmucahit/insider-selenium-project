# Insider QA - Case Study

### **Case Study**

1. Visit the Insider home page ([https://useinsider.com/](https://useinsider.com/)) and check if it is opened.
2. Select the “Company” menu in the navigation bar, choose “Careers,” and verify if the Career page is opened.
   Additionally, check if the Locations, Teams, and Life at Insider blocks are visible.
3. Navigate to the Quality Assurance
   page ([https://useinsider.com/careers/quality-assurance/](https://useinsider.com/careers/quality-assurance/)), click
   on "See all QA jobs," filter the jobs by Location: “Istanbul, Turkey,” and Department: “Quality Assurance.” Verify
   the presence of the job list.
4. Ensure that all jobs' Position contains “Quality Assurance,” Department contains “Quality Assurance,” and Location
   contains “Istanbul, Turkey.”
5. Click the “View Role” button and verify that this action redirects to the Lever Application form page.

# Project Details

Bu proje UseInsider sitesi için UI otomasyon testlerini içerir. Anasayfa, Careers ve QualityAssurcePage sayfaları için
test case’ler hazırlanmıştır. Proje Python’ın Pytest Kütüphanesi kullanılarak yazılmıştır. Chrome ve Mozilla
tarayıcılarında testler koşulmaktadır.

### Project Video

[Testing Videos (Youtube)](https://youtu.be/SBDv5bda5rM)

## Folder Structure

    |   .env
    |   .gitignore
    |   README.md
    |   report.html
    |   requirements.txt
    |   testing_video.mp4   
    +---assets
    |   |   style.css
    |   |   
    +---configs
    |   |   constants.py
    |   |   __init__.py
    |   |   
    +---pages
    |   |   base.py
    |   |   careersPage.py
    |   |   homePage.py
    |   |   qualityAssurancePage.py
    |   |   __init__.py
    |   |   
    +---testCases
    |   |   test_base.py
    |   |   test_careersPage.py
    |   |   test_homePage.py
    |   |   test_qualityAssurancePage.py
    |   |   __init__.py

---
**config/:** Projenin konfigürasyon dosyalarının bulunduğu klasör.

- **init.py:** WebDriver'ın konfigürasyonun olduğu dosya.
- **constants.py:** Sabit değişkenlerini bulunduğu dosya.

**pages/:** Test yazılırken sayfalara özel kullanılacak methodların bulunduğu klasör.

- **base.py:** Her test senaryolarında kullanabilecek global methodları içeren dosya. Sayfalara özel classlar bu dosya
  içindeki class'tan kalıtım alır.
- **homePage.py:** Ana sayfaya (HomePage) özel methodların bulunduğu dosya.
- **careersPage.py:** Kariyer sayfasına (CareersPage) özel methodların bulunduğu dosya.
- **qualityAssurancePage.py:** Quality Assurance sayfasına (QualityAssurancePage) özel methodların bulunduğu dosya.
  **testCases/:** Test case'lerin bulunduğu klasör.
- **test_base.py:** config/init.py içinde tanımlanan WebDriver bu dosya içinde fixture olarak işaretlenir. Bu sayede tüm
  test caselerde bu driver argüman olarak tanımlanır.
- **test_homePage.py:** Ana sayfa (HomePage) ile ilgili test case'leri içeren dosya.
- **test_careersPage.py:** Kariyer sayfası (CareersPage) ile ilgili test case'leri içeren dosya.
- **test_qualityAssurancePage.py:** Quality Assurance sayfası (QualityAssurancePage) ile ilgili test case'leri içeren
  dosya.

![flow](flow.png)

## Run Command

    pytest -v --html=report.html

# Test Steps

### test_homePage.py

Bu test dosyasında 2 adet test bulunmaktadır.

1. Test:
    - ([https://useinsider.com/](https://useinsider.com/)) sayfasını açar.
    - Eğer cookie uyarısı varsa, kapatır.
    - Daha sonra `router.home-page` elementinin varlığını kontrol eder.
    - Eğer varsa, test başarılı olur.
2. Test:
    - Company header menüsünden "**Company**" butonuna tıklanır.
    - Ardından açılan menüden "**Careers**" butonuna tıklanır.
    - `router.career-page` elementinin varlığını kontrol eder.
    - Eğer varsa, test başarılı olur.

### test_careerPage.py

Bu dosyada 3 adet test bulunmaktadır:

1. Test:
    - Career sayfasını açar
    - Eğer cookie uyarısı varsa, kapatılır
    - Sayfada lokasyonlara scroll yapılır (`0.7` saniye beklenir, scroll animasyonlu bir şekilde yapıldığı için. kod 0.7
      saniye bekletilir)
    - `actual_our_locations_list` adlı boş bir liste oluşturulur.
    - Lokasyonlar bu liste eklenir.
    - `result_location_list` constant ile karşılaştırılır.
    - Eğer sonuçlar aynıysa, test başarılı olur.
2. Test:
    - Departman listesine scroll yapılır (`0.7` saniye beklenir, scroll animasyonlu bir şekilde yapıldığı için. kod 0.7
      saniye bekletilir).
    - See All Teams butonuna tıklanır.
    - `actual_departments_list` adlı boş bir liste oluşturulur.
    - Departmanlar bu liste eklenir.
    - `result_departments_list` constant ile karşılaştırılır.
    - Eğer sonuçlar aynıysa, test başarılı olur.
3. Test:
    - Sayfadaki "**Life at Insider**" kısmının varlığı kontrol edilir.

### test_qualityAssurancePage.py

Bu sayfada 5 tane test bulunmaktadır:

1. Test:
    - Quality Assurance sayfasını açar.
    - Eğer cookie uyarısı varsa, kapatılır.
    - See All QA Jobs butonuna tıklanır.
    - Lokasyon dropdown'ından "**Istanbul, Turkey**" seçilir.
    - Dropdown'da "**Istanbul, Turkey**" seçili mi kontrol edilir.
2. Test:
    - Departman olarak Quality Assurance seçilir.
    - Departman dropdown'ında "**Quality Assurance**" seçili mi kontrol edilir.
3. Test:
    - Dropdown'lar seçildikten sonra job list'in varlığı kontrol edilir.
4. Test:
    - Tüm iş ilanlarının İstanbul, Türkiye konumunda ve Quality Assurance pozisyonunda olduğu kontrol edilir.
5. Test:
    - Pozisyonlara scroll yapılır (`1` saniye beklenir, scroll animasyonlu bir şekilde yapıldığı için. kod 1 saniye
      bekletilir).
    - "**View Role**" mouse hover özelliği ile görünür olduğu için, pozisyona focus olunur.
    - Pozisyonun başlığı değişkene atanır. (İlandaki başlığa göre karşılaştırılacak)
    - "**View Role**" butonuna tıklanır.
    - Yeni sekmede Lever ilanı açılır.
    - Driver, Lever sekmesine geçiş yapar.
    - Leverdaki ilanın başlığı değişkene atanır.
    - Pozisyonun başlığı ve Leverdaki ilanın başlığı karşılaştırılır.
    - Tüm işlemler her bir pozisyon için tekrar kontrol edilir.
    - Eğer liste uyumsuzluk yoksa, test başarılı olur.