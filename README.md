# MyVideo
MyVideo - проект для выходного тестирования в лабораторию. Он представляет собой простой Django-проект, с подключенной к нему развитой системой управления контентом Wagtail. Присутствует
минимальное rest api для получения списка видео,
исполнения информации по каждому. При загрузке видео
оно конвертирует в 4 формата 360, 480, 720, 1080
, чтобы 

## Запуск
``` bash
pip install -r requirements.txt 
sudo apt-get update 
sudo apt install python3-opencv 
python manage.py migrate 
python manage.py shell -c "import prepare"
```

