package credentialValidationProgram.application;
// Library of Java utility, class Scanner.
import java.util.Scanner;

public class Program {

	public static void main(String[] args) {
		// Scanner Class
		// sc = Object Scanner
		// new = New instance of Scanner
		// System.in = Entering data.
		Scanner sc = new Scanner(System.in);
		
		while (true) {
			System.out.print("Login: ");
			String login = sc.nextLine();
			System.out.print("Password: ");
			String password = sc.nextLine();
			if (!(login.equals("johnlennon") && password.equals("imagineworld33"))) {
				System.out.println("Invalid Credentials");
				continue;
			}
			else {
				System.out.println("Welcome to Matrix33 Server");
				sc.close();
				break;
			}
			
		}

	}

}
