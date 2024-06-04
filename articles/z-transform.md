# Study and examination of z-transform

## 3D gnuplot for z-transform

It is said on text book that it is close to fourier transform for r = 1.0. However, for 1 > 1.0, for the author, it seems it is close to descreate laplace transform esp. with n > 0. Thus, the author think it is appropriate to use z-trans to digital control.

![z-trans for sin t and sin 100t](/articles/img/z-trans-sin.png "z-trans for sin t and sin 100t")

$x(n) = \sin n + \sin 100n$

Why r > 1.0 for many r? It seems it is multiple laplace transform. It means Z(x(n)) := set of laplace transform for digital. If it were analysis, is s and $1/(s + 2)$ for instance. It could be supposed that since it is numeric, set of digital laplace transform is utilized.

![z-trans for sin t and sin 100t](/articles/img/r0_1.png "z-trans for sin t and sin 100t")

$r_{initital} = 0.1$ It is high digit for r lower. Thus, only row r spectrum is seems shown. Actually, for other r, there are no flat spectrum. $x(n) = \sin n + \sin 100n$ / Why this shape of spectrum? How about gain if it were used for transfer function of digital control?

![z-trans for sin t and sin 100t](/articles/img/r0_5.png "z-trans for sin t and sin 100t")

$r_{init} = 0.5$. It is interesting that yet another shape of power spectrum is obtained for different r. It is about transfer function but digital filter as well. In that sense ,what is digital filter for audio analysis, then?

![z-trans for sin t and sin 100t](/articles/img/log-power.png "z-trans for sin t and sin 100t")

$\log_{10}$ of power from $r_{init} = 0.1$ . $log_{10}$ of powers is obtained. It can be seen that digit is from 100 to 1. Gains for any r is low thus it goes to flat for $log$. It can be seen that amplitude of gain of $X(z)$ gets lower with respect to r lower. Analysis of z-transform says that $n = -\inf to \inf$. But as numerical calculation, is it really possible to calc? Is there some mistake for author's understanding and/or impl of z-trans?