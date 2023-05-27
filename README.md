# product_search_service_demo

## Useful commands just for me :)
cd D:\Redis-x64-3.2.100
cd C:\Users\Sina\Desktop\project\src
workon demo-back-py310
celery -A config worker -l INFO -P eventlet
celery -A config worker -l INFO -P gevent

pytest e2e/test_apis.py::test_uploadImage
