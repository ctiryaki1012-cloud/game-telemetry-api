# API Tasarım Dokümanı

## Proje Amacı

Bu projede FastAPI kullanarak basit bir backend API geliştirmek istedim. İlk hafta API'nın çalışıp çalışmadığını kontrol eden /health ve oyun olaylarını kabul eden /events endpoint'lerini oluşturdum.

## Endpointler

### GET /health
Backend'in çalışıp çalışmadığını kontrol eder.

Yanıt:
{
    "status": "ok"
}

### POST /events
Oyundan gelen event bilgisini kabul eder.

Yanıt:

{
    "message": "Event alındı."
}
## Olay Şeması

İleride API'nin kabul edeceği olay verilerinin alanları bu bölümde tanımlanacaktır.