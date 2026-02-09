# Multi-Agent Workshop

Bu proje, Google Cloud üzerinde çalışan çoklu ajan (multi-agent) sistemlerini göstermek için hazırlanmıştır.

## Google Cloud Shell Kurulumu

Projeyi Google Cloud Shell üzerinde çalıştırmak için aşağıdaki adımları takip edebilirsiniz:

### 1. Projeyi Klonlayın

Terminali açın ve projeyi bilgisayarınıza indirin:

```bash
git clone https://github.com/nisailhan/multi-agent-workshop.git
cd multi-agent-workshop
```

### 2. Sanal Ortam Oluşturun (Önerilen)

Bağımlılıkların çakışmasını önlemek için sanal bir Python ortamı oluşturun ve aktif edin:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Gerekli Kütüphaneleri Yükleyin

Projenin çalışması için gerekli olan `google-adk` ve `google-genai` kütüphanelerini yükleyin:

```bash
pip install -r requirements.txt
```

### 4. API Anahtarını Tanımlayın

Google AI Studio'dan aldığınız API anahtarını tanımlayın. (Güvenlik için API anahtarınızı asla doğrudan kodun içine yazıp commit etmeyin):

```bash
export GOOGLE_API_KEY="YOUR_API_KEY_HERE"
```

*Not: `"YOUR_API_KEY_HERE"` kısmını kendi API anahtarınızla değiştirmeyi unutmayın.*

### 5. Projeyi Çalıştırın

Artık ajanları çalıştırabilirsiniz. Örneğin, manuel orkestrasyon betiğini çalıştırmak için:

```bash
python manual_orchestration_script.py "Generative AI hakkında bilgi ver"
```

Veya kendi yazdığınız başka bir komutu deneyebilirsiniz.

## Proje Yapısı

- `agent.py`: Ana orkestratör ajanı tanımları.
- `analyst/`, `researcher/`, `planner/`: Alt ajanların klasörleri.
- `manual_orchestration_script.py`: Ajanları manuel olarak sırayla çalıştıran örnek betik.
