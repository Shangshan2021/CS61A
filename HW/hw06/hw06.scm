(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)


(define (sign num)
  (cond ((= 0 num) 0) ((< 0 num) 1) (else -1))
)


(define (square x) (* x x))


(define (pow x y)
  (cond ((= 1 x) 1) ((= 0 y) 1) (else (* x (pow x (- y 1)))))
)

