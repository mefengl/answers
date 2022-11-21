const combine = (...fs) => {
  return (x) => {
    return fs.reduceRight((acc, f) => f(acc), x);
  };
}

const say = (stentence) => {
  console.log(stentence);
}

const sayHi = (stentence) => {
  return "hi " + stentence;
}

const sayBye = (stentence) => {
  return "bye " + stentence;
}

const sayName = (name) => {
  return "my name is " + name;
}

const sayHello = combine(say, sayHi, sayBye, sayName);

sayHello("John");
