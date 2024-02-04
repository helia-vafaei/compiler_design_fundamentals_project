// Class representing a University that is coupled with the City class
class University {
    private String ID;
    private String name;
    private City city;

    public University(String ID, String name, City city) {
        this.ID = ID;
        this.name = name;
        this.city = city;
    }

    public String getID() {
        return ID;
    }

    public String getName() {
        return name;
    }

    public City getCity() {
        return city;
    }

}

// Class representing a Student that is coupled with the University class
class Student {
    private String FirstName;
    private String LastName;
    private University uni;

    public Student(String FirstName, String LastName, University uni) {
        this.FirstName = FirstName;
        this.LastName = LastName;
        this.uni = uni;
    }

    public String getFirstName() {
        return FirstName;
    }

    public String getLastName() {
        return LastName;
    }

    public University getUniversity() {
        return uni;
    }
}

// Class representing a City
class City {
    private String name;

    public City(String name) {
        this.name = name;
    }

    public String getName() {
        return name;
    }
}

public class Main {
    public static int sum(int a, int b) {
        return a + b;
    }
    public static void main(String[] args) {
        City city = new City("tehran");

        // Creating an instance of the University class
        University uni = new University("99521271", "IUST", city);

        // Creating an instance of the Student class and associating it with the
        // University
        Student student = new Student("Farzan", "Rahmani", uni);

        // Printing the student's first name, last name, and the name of the
        // university
        System.out.println("First Name: " + student.getFirstName());
        System.out.println("Last Name: " + student.getLastName());
        System.out.println("University: " + student.getUniversity().getName());

        int a = 7 + 8;
        int b = 3 * 2;
        if(a < b)
        {
            b = 9;
        }
        for(int i = 0; i < 100; i++)
        {
            b += i * 1.5;
        }

        int c = sum(12, 89);
    }
}
