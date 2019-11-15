What is the difference between poll, epoll and select?

select() was introduced in BSD Unix, and was probably the first API in Unix to check for file descriptor readiness. poll() was introduced a bit later, and in the System V sub-family of Unix. Both were later adopted in POSIX. Functionally they are very similar: You pass them a bunch of file descriptors—typically of sockets—as well as a timeout value, and the system will tell you when/whether anything "interesting" happened on them: when an FD has something for you to read(), or when it becomes possible to write(), or when some sort of exception happened. select() uses three bitmaps (read/write/error) to represent the file descriptors of interest, which is quite compact (less data to pass across user/kernel boundary) but limits the number of file descriptors that it can support. poll() uses vectors of {file descriptor+set of situations-of-interest}, and can thus support large numbers of active file descriptors, though its overhead can be significant. Another difference is that select() modifies the user-supplied file descriptor bitmaps in place to signal which sockets are ready, while poll() has separate fields of input ("of interest") and output events per-socket.

epoll is a Linux-specific enhancement of poll(). It hides the details of representation in an internal data structure that is manipulated using a special function epoll_create().

======================================================================

