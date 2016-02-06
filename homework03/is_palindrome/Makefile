CC=		gcc
CFLAGS=		-c -g -pgmake
LD=		gcc
LDFLAGS=	-shared
AR=		ar
ARFLAGS=	rcs
TARGETS=	is_palindrome

all:	$(TARGETS)

is_palindrome: is_palindrome.c
	gcc -g -gdwarf-2 -pg is_palindrome.c -o is_palindrome
    
test:
	./is_palindrome < is_palindrome.input > real.output
	diff real.output is_palindrome.output

clean:
	rm -f $(TARGETS) *.o
