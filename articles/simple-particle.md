# Micro mechanics approach to fluid dynamics. Simple to Complex

When I was under grad student, I studied fluid dynamics and thermo dynamics. There were PDE. How is it analysed? Harmonic analysis? So what? I know about FEM but I thought it is just calculation. What can be known by just calculation? Then, I stopped to study fluid dynamics.

Now, I know the power of numerical calculation and hypotheis driven. I studied enough amount of control engineering and material mechanics. Then, I think it is good timing to study and reserch fluid dynamics.

In this report and repository, some kind of study and reserach will be taken. The methodolody is assumed to be hypothesis driven physical modelling and micro-mechanics apparoch and visualizing with numerical simulation using Python and OpenGL/GLUT.

It could be said that C++ is faster than Python. However, considering educational effect and openness to every one, Python would be utilized.

# Differential Equation and application

Vehicle. Aeroplane. Drone. There are a many applications in industry which require fluid dynamics for research. In this rep, micro mechanical methodology is taken to modelling of fluid and mainly, vehicle or bycle as a application, simulation would be taken. Ultimately, it would be shown that air-flow with some shape of disk-wheel or composite-wheel, it would be make flow of air better for high performance of vehicle and bicycle. Drone dev could deploy this simulator to research/study their fluid.

# Order of calculation. LL and C++

It works. This OO simulator works. Lego-blocking approach of component is fun and high productivity. In this first version of simulator with Simple Particle, 100 or 200 particle are max and it is not possible to do real time rendering by 1000 particles. It is assumed to be 3 reasons.

1. order of calc with simple particle manager. All particle has effect from all particles which is O(n^2).
2. Particles require many call of vertex which is open GL function to render circle. Polygon might be enough.
3. Multi core processing. It seems that python could be used by multi core processing by some method.
4. Cython? Final option.

Someone could argue that MacBook Pro and M4Max would be better choice. It could be but I think it could be different. Ultimately, numerical calculation could be 1 week to calc. In that time, mac studio or server is better choice. If it were less than 5 min or real time, it is OK to use pro. However, I suppose to use combination of MacbookAir and studio or GPU cluster on AWS.

# Research log

It is interesting too see trajectory of particle with different class of differential equation. If there are dumper, it goes to origin.

Setting of num calc has been changed. The more particle and the more far ortho, it gets close to particle. Around 200 particles may be limit by python. Is it should be C++ or split simulator and visualizer to different program? The author thinks several bottle neck of this simular is better to be resolved such as order of particle manager.

It seems there are equibrium for enought number of particles and thus, not so much oscillation.

## Simple 100 Particle with reflection hypothesis

![100 particles with reflection](/articles/img/si-100.png "100 particles with reflection")

*At this time, img cannot be shown. It would be fixed later.*

In this figure, it is shown that if there are many particle, they are on equilibrium and not moved their relative position. It might be as a result of spring type ODE per particle and gravity with particle to particle.

It would be said that it is close to real water since which has H-bonding with H2O melecular. The more particles, the more close to molecular and then, it make some of cells in micro mechanics or solid state physics and then, goes to equibrium.

It might be interesting to see the effect of amplitude of gravity. If they goes to higher, it would be close to solid material. If not, it would be close to be liquid or air.
