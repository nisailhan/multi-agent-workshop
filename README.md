# Multi-Agent Workshop

Bu proje, Google Cloud üzerinde çalışan çoklu ajan (multi-agent) sistemlerini göstermek için hazırlanmıştır.

## Kurulum (Setup)

Örnekleri çalıştırmadan önce, Cloud Shell veya yerel `gcloud` kurulumunuzda aşağıdaki adımları tamamladığınızdan emin olun.

### 1. Google Cloud Projesini Ayarlayın (gcloud Config)

Projenizin seçili olup olmadığını kontrol edin:

```bash
gcloud config list
```

Çıktıda `project = your-google-cloud-project-id` görmelisiniz. Eğer ayarlı değilse, proje ID'nizi ayarlayın:

```bash
gcloud config set core/project your-google-cloud-project-id
```

Eğer Cloud Shell'de değilseniz (yerel bilgisayarınızda çalışıyorsanız), kimlik doğrulaması yapın:

```bash
gcloud auth application-default login
```

### 2. Vertex AI API'yi Etkinleştirin

```bash
gcloud services enable aiplatform.googleapis.com
```

### 3. Kodu İndirin (Get the Code)

Repository'i klonlayın:

```bash
git clone https://github.com/nisailhan/multi-agent-workshop.git
```

### 4. Python Ortamını Hazırlayın

Proje klasörüne gidin, sanal ortam oluşturun ve aktif edin:

```bash
cd multi-agent-workshop
python3 -m venv .venv
source .venv/bin/activate
```

Gerekli kütüphaneleri (ADK ve diğerleri) yükleyin:

```bash
pip install -r requirements.txt
```

### 5. Google AI veya Vertex AI Konfigürasyonu

Google AI (Gemini API Key) veya Vertex AI kullanmak için ortam değişkenlerini ayarlamanız gerekmektedir.

**Vertex AI için Örnek Konfigürasyon:**

Bir `.env` dosyası oluşturun veya aşağıdaki değişkenleri export edin:

```bash
export GOOGLE_GENAI_USE_VERTEXAI=TRUE
export GOOGLE_CLOUD_PROJECT=your-google-cloud-project-id
export GOOGLE_CLOUD_LOCATION=us-central1
```

**Google AI Studio (API Key) Kullanacaksanız:**

```bash
export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

## Projeyi Çalıştırma

Tüm ayarlamalar bittikten sonra projeyi çalıştırabilirsiniz.

**Manuel Orkestrasyon Örneği:**

```bash
python manual_orchestration_script.py "Generative AI hakkında bilgi ver"
```
