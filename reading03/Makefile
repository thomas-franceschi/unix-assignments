all: hello-dynamic hello-static hello-debug hello-profile

hello-dynamic: 

hello-static: 
    gcc -static hello.c

hello-debug: 
    gcc -g hello.c

hello-profile: 
    gcc -pg hello.c

clean: 
    rm hello-*