CC=		gcc
CFLAGS=		-c
LD=		gcc
LDFLAGS=	-shared
AR=		ar
ARFLAGS=	rcs
TARGETS=	libgcd.a libgcd.so gcd-static gcd-dynamic

all:	$(TARGETS)

gcd-dynamic: main.o libgcd.so
	$(LD) -o $@ -L. $^ -lgcd
    
gcd-static: main.o libgcd.a
	$(LD) -static -o $@ -L. $^ -lgcd

libgcd.so: gcd.o
	$(LD) $(LDFLAGS) -o $@ $^
    
libgcd.a: gcd.o
	$(AR) $(ARFLAGS) $@ $^

%.o: %.c
	$(CC) $(CFLAGS) -o $@ $^

clean:
	rm -f $(TARGETS) *.o
