package animals;

public class Fish implements Prey, Predator {

	@Override
	public void hunt() {
		System.out.println("Bigger fish chasing smaller fish");
		
	}

	@Override
	public void flee() {
		System.out.println("Smaller fish running away from a bigger fish");
		
	}

}
