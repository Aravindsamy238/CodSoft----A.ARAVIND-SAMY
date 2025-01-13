import java.util.Scanner;

public class ContentBasedRecommendation {

    public static void main(String[] args) {
       String[] books = {"Book 1", "Book 2", "Book 3", "Book 4", "Book 5"};
        double[][] bookGenres = {
            {5, 1, 2, 4, 3},                  
            {3, 5, 1, 2, 4},                       
            {4, 3, 3, 5, 2},                                      
            {1, 4, 5, 3, 4},                  
            {5, 2, 4, 1, 5}                                 
        };
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter your ratings for the following genres (1 to 5):");
        System.out.print("Fiction: ");
        double fiction = scanner.nextDouble();
        System.out.print("Mystery: ");
        double mystery = scanner.nextDouble();
        System.out.print("Romance: ");
        double romance = scanner.nextDouble();
        System.out.print("Sci-Fi: ");
        double scifi = scanner.nextDouble();
        System.out.print("Fantasy: ");
        double fantasy = scanner.nextDouble();
        double[] userPreferences = {fiction, mystery, romance, scifi, fantasy};

        double[] similarities = new double[books.length];
        for (int i = 0; i < books.length; i++) {
            similarities[i] = cosineSimilarity(userPreferences, bookGenres[i]);
        }
        System.out.println("\nTop 3 Recommended Books:");
        for (int i = 0; i < 3; i++) {
            int maxIndex = getMaxSimilarityIndex(similarities);
            System.out.println(books[maxIndex] + " with similarity: " + similarities[maxIndex]);
            similarities[maxIndex] = -1; // Mark this book as processed
        }

        scanner.close();
    }
    public static double cosineSimilarity(double[] userPreferences, double[] bookGenres) {
        double dotProduct = 0;
        double userMagnitude = 0;
        double bookMagnitude = 0;
        for (int i = 0; i < userPreferences.length; i++) {
            dotProduct += userPreferences[i] * bookGenres[i];
            userMagnitude += Math.pow(userPreferences[i], 2);
            bookMagnitude += Math.pow(bookGenres[i], 2);
        }
        userMagnitude = Math.sqrt(userMagnitude);
        bookMagnitude = Math.sqrt(bookMagnitude);

        if (userMagnitude == 0 || bookMagnitude == 0) {
            return 0;
        }

        return dotProduct / (userMagnitude * bookMagnitude);
    }
    public static int getMaxSimilarityIndex(double[] similarities) {
        int maxIndex = -1;
        double maxSimilarity = -1;
        for (int i = 0; i < similarities.length; i++) {
            if (similarities[i] > maxSimilarity) {
                maxSimilarity = similarities[i];
                maxIndex = i;
            }
        }
        return maxIndex;
    }
}
