PROGRAM = Program
# MODULES = modules
# Compile options. Το -I<dir> λέει στον compiler να αναζητήσει εκεί include files
CFLAGS = -Wall -no-pie -fPIE -g -I$(INCLUDE)

# Αρχεία .o
OBJS = $(PROGRAM)/tic


# the executable program
# EXEC = csp

# $(EXEC):
#	python3 $(OBJS)

# clean:
# rm -rf __pycache__

run: $(EXEC)
	python3 $(PROGRAM)/tic.py
