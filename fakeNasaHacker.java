class Main {
  public static void main(String[] args) throws InterruptedException {
    int repeater = 0;
    while (repeater < 11) {
      System.out.println("Hacking NASA - " + repeater*10 + "%");
      repeater += 1;
      Thread.sleep(1000);
    }
    System.out.println("Hacked Nasa successfully");
  }
}
