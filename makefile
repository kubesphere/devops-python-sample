run:
	docker build -f Dockerfile-online -t shaowenchen/demo .
	docker run -d -p 8011:8000 --name python-demo shaowenchen/demo
test:
	curl localhost:8011
stop:
	docker stop python-demo
	docker rm python-demo
