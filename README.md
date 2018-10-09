# SignalReverb

Disclaimer: I started this project because I wanted to see what my favorite songs would sound like in various different concert halls, venues, stadiums, etc. This is purely an exploratory project and is by no means comprehensive.

## Background
Indoor music venues can be thought of as Linear and Time Invariant (LTI) systems. LTI systems have 2 defining properties:
* Linearity: There is a linear mapping between the input and output (i.e. <a href="https://www.codecogs.com/eqnedit.php?latex=x_1(t)&space;\rightarrow&space;y_1(t),&space;x_2(t)&space;\rightarrow&space;y_2(t)&space;\implies&space;ax_1(t)&space;&plus;&space;bx_2(t)&space;\rightarrow&space;ay_1(t)&space;&plus;&space;by_2(t)" target="_blank"><img src="https://latex.codecogs.com/gif.latex?x_1(t)&space;\rightarrow&space;y_1(t),&space;x_2(t)&space;\rightarrow&space;y_2(t)&space;\implies&space;ax_1(t)&space;&plus;&space;bx_2(t)&space;\rightarrow&space;ay_1(t)&space;&plus;&space;by_2(t)" title="x_1(t) \rightarrow y_1(t), x_2(t) \rightarrow y_2(t) \implies ax_1(t) + bx_2(t) \rightarrow ay_1(t) + by_2(t)" /></a>)
* Time Invariance: Delaying an input by T delays the output by T (i.e. $$x(t) \rightarrow y(t) \implies x(t-T) \rightarrow y(t-T)$$)

$$x_1(t)$$
