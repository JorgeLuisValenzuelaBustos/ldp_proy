import 'dart:async';

int numInt = 1;
double numDou = 2.0;

int add(int value) {
  return numInt += value;
}

double sub(num value) {
  return numDou -= value;
}

String EXPERIENCIA = 'EXP';

List<String> lista = List.filled(2, "a");
Map<String, int> mapa = new Map<String, int>();

var left = 1.2;
double width = 1.1;
set right(double value) => left = value - width;

const initialCapacity = 16;
typedef IntList = List<int>;



