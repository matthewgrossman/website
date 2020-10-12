install:
	npm install

serve:
	npx @11ty/eleventy --serve

build:
	npx @11ty/eleventy

publish: build
	echo "blah"
