public class Fibonnaci {
    public static void printFibonacci(Integer n) {
        Integer a = 0;
        Integer b = 1;

        System.debug('Fibonacci Series up to ' + n + ' terms:');
        for (Integer i = 0; i < n; i++) {
            System.debug(a);
            Integer temp = a + b;
            a = b;
            b = temp;
        }
    }
}

//Fibonnaci.printFibonacci(7);
