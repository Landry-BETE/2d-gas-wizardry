# pygas2d
I've always had a hard time visualizing physics. Python seems to be a good way of overcoming this limitation. 
I had fun doing it and I hope you will too.

## Getting Started

### Prerequisites

Object oriented programming with Python, Pygame basics and Numpy

### Installing

It should be fast:

If you have pip, you can install pygame first

```
pip install pygame
```

And then numpy(in order to compute speed changes after collisions)

```
pip install numpy
```

Video demo(coming)


## Debugging/tests

For each frame, the program outputs to the console the total kinetic energy, remaining momentum of
the gas and momentum exchanged with the walls (up to a constant multiplier). You might want to put
that into a log file or a database but be aware that those I/O operations can negatively impact the perceived framerate.
Until someone comes up with proper tests, you'll have to trust me when I say "it works" :) 

<!---### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

--->

## Built With

* [Python](http://www.python.org) - The programming language used
* [Numpy](http://www.numpy.org/) - Scientific Computing, Multivariable calculus
* [Pygame](https://www.pygame.org/) - Used as a graphical library

## Contributing

In so far as you respect the terms of the license, do whatever you want. There are no rules...yet :)

## Authors

* **Landry BETE** - *Initial work* - [Landry-BETE](https://github.com/Landry-BETE)

<!---See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.--->

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Harrion Kinsley](https://github.com/Sentdex)(Sentdex), who makes really great Python tutorials!
* Stubbornness, when I face weird bugs(apparent energy loss during the development)
* Someone else I probably forgot
