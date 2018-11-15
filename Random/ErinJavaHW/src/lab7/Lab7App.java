package lab7;
/**
 * <p>Title: The Lab7App class</p>
 *
 * <p>Description: This class will be used to thoroughly test the 
 * various methods in the PokerHand class.  The seven cards specified 
 * will be used to test each method.</p>
 *
 * @author your name here
 */
public class Lab7App
{
    /**
     * <p> Name: main method </p>
     * 
     * @param args values to be sent to the method
     */
	public static void main(String[] args)
	{
		testFourOfAKind();
		testFlush();
		testThreeOfAKind();
		testPair();
		testLowCard();
    }
    
    /**
     * <p> Name: testFourOfAKind method </p>
     * 
     * <p> Description: tests the fourOfAKind method in the PokerHand class.</p>
     */
	public static void testFourOfAKind()
	{
		// cards to be used to test the various methods
		// in the PokerHand class
		Card twoClubs = new Card(2);
		Card twoDiamonds = new Card(15);
		Card twoHearts = new Card(28);
		Card twoSpades = new Card(41);
		Card threeClubs = new Card(3);
		Card fourClubs = new Card(4);
		Card fiveClubs = new Card(5);
		PokerHand hand = new PokerHand(twoClubs,twoDiamonds,twoHearts,twoSpades);
		
		System.out.println("Testing fourOfAKind method:");
		System.out.println(hand);
		
		if (hand.fourOfAKind()) {
			System.out.println("Four of a kind");
		} else {
			System.out.println("Not four of a kind");
		}
		System.out.println();
		hand.replaceCard(2,threeClubs);
		System.out.println("Replaced the 2 of diamonds with the 3 of clubs:");
		System.out.println(hand);
		if (hand.fourOfAKind()) {
			System.out.println("Four of a kind");
		} else {
			System.out.println("Not four of a kind");
		}
		System.out.println();
	}
	
    /**
     * <p> Name: testFlush method </p>
     * 
     * <p> Description: tests the flush method in the PokerHand class.</p>
     */
	public static void testFlush()
	{
		// cards to be used to test the various methods
		// in the PokerHand class
		Card twoClubs = new Card(2);
		Card twoDiamonds = new Card(15);
		Card twoHearts = new Card(28);
		Card twoSpades = new Card(41);
		Card threeClubs = new Card(3);
		Card fourClubs = new Card(4);
		Card fiveClubs = new Card(5);
		PokerHand hand = new PokerHand(twoClubs,threeClubs,twoHearts,twoSpades);
		
		System.out.println("Testing flush method:");
		System.out.println();
		System.out.println(hand);
		
		if (hand.fourOfAKind()) {
			System.out.println("Flush");
		} else {
			System.out.println("Not a flush");
		}
		
		System.out.println();
		hand.replaceCard(3,fourClubs);
		hand.replaceCard(4,fiveClubs);
		System.out.println("Replaced the 2 of hearts with the 4 of clubs and the 2 of spades with the 5 of clubs:");
		System.out.println(hand);
		if (hand.flush()) {
			System.out.println("Flush");
		} else {
			System.out.println("Not a flush");
		}
		System.out.println();
	}
	
    /**
     * <p> Name: testThreeOfAKind method </p>
     * 
     * <p> Description: tests the threeOfAKind method in the PokerHand class.</p>
     */
	public static void testThreeOfAKind()
	{
		// cards to be used to test the various methods
		// in the PokerHand class
		Card twoClubs = new Card(2);
		Card twoDiamonds = new Card(15);
		Card twoHearts = new Card(28);
		Card twoSpades = new Card(41);
		Card threeClubs = new Card(3);
		Card fourClubs = new Card(4);
		Card fiveClubs = new Card(5);
		
		PokerHand hand = new PokerHand(twoClubs,threeClubs,fourClubs,fiveClubs);
		
		System.out.println("Testing threeOfAKind method:");
		System.out.println();
		
		System.out.println(hand);
		
		if (hand.threeOfAKind()) {
			System.out.println("Three of a kind");
		} else {
			System.out.println("Not three of a kind");
		}
		
		System.out.println();
		
		hand.replaceCard(2,twoDiamonds);
		hand.replaceCard(3,twoHearts);
		
		System.out.println(hand);
		if (hand.threeOfAKind()) {
			System.out.println("Three of a kind");
		} else {
			System.out.println("Not three of a kind");
		}
		
		System.out.println();
		hand.replaceCard(3, threeClubs);
		hand.replaceCard(4, twoHearts);
		System.out.println(hand);
		if (hand.threeOfAKind()) {
			System.out.println("Three of a kind");
		} else {
			System.out.println("Not three of a kind");
		}
		
		System.out.println();
		hand.replaceCard(2, threeClubs);
		hand.replaceCard(3, twoDiamonds);
		System.out.println(hand);
		if (hand.threeOfAKind()) {
			System.out.println("Three of a kind");
		} else {
			System.out.println("Not three of a kind");
		}
		
		System.out.println();
		hand.replaceCard(1, threeClubs);
		hand.replaceCard(2, twoClubs);
		System.out.println(hand);
		if (hand.threeOfAKind()) {
			System.out.println("Three of a kind");
		} else {
			System.out.println("Not three of a kind");
		}
		System.out.println();
	}
	
    /**
     * <p> Name: testPair method </p>
     * 
     * <p> Description: tests the pair method in the PokerHand class.</p>
     */
	public static void testPair()
	{
		// cards to be used to test the various methods
		// in the PokerHand class
		Card twoClubs = new Card(2);
		Card twoDiamonds = new Card(15);
		Card twoHearts = new Card(28);
		Card twoSpades = new Card(41);
		Card threeClubs = new Card(3);
		Card fourClubs = new Card(4);
		Card fiveClubs = new Card(5);
		
		PokerHand hand = new PokerHand(twoClubs,threeClubs,fourClubs,fiveClubs);
		
		System.out.println("Testing pair method:");
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}
		
		hand.replaceCard(2,twoDiamonds);
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}

		hand.replaceCard(2, fourClubs);
		hand.replaceCard(3,twoDiamonds);
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}
		
		hand.replaceCard(3, fiveClubs);
		hand.replaceCard(4,twoDiamonds);
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}
		
		hand.replaceCard(1, fiveClubs);
		hand.replaceCard(2, twoClubs);
		hand.replaceCard(3, twoDiamonds);
		hand.replaceCard(4, fourClubs);
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}
		
		hand.replaceCard(3, fourClubs);
		hand.replaceCard(4, twoDiamonds);
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}
		
		hand.replaceCard(2, fourClubs);
		hand.replaceCard(3, twoClubs);
		System.out.println();
		System.out.println(hand);
		if (hand.pair()) {
			System.out.println("Pair");
		} else {
			System.out.println("Not a pair");
		}
		System.out.println();
	}
	
    /**
     * <p> Name: testLowCard method </p>
     * 
     * <p> Description: tests lowCard method in the PokerHand class.</p>
     */
	public static void testLowCard()
	{
		// cards to be used to test the various methods
		// in the PokerHand class
		Card twoClubs = new Card(2);
		Card twoDiamonds = new Card(15);
		Card twoHearts = new Card(28);
		Card twoSpades = new Card(41);
		Card threeClubs = new Card(3);
		Card fourClubs = new Card(4);
		Card fiveClubs = new Card(5);
		
		PokerHand hand = new PokerHand(twoClubs,threeClubs,fourClubs,fiveClubs);
		
		System.out.println("Testing lowCard method:");
		System.out.println();
		System.out.println(hand);
		System.out.println("The low card is " + hand.lowCard());
		System.out.println();

		hand.replaceCard(1, threeClubs);
		hand.replaceCard(2, twoClubs);
		System.out.println(hand);
		System.out.println("The low card is " + hand.lowCard());
		System.out.println();

		hand.replaceCard(2, fourClubs);
		hand.replaceCard(3, twoClubs);
		System.out.println(hand);
		System.out.println("The low card is " + hand.lowCard());
		System.out.println();

		hand.replaceCard(3, fiveClubs);
		hand.replaceCard(4, twoClubs);
		System.out.println(hand);
		System.out.println("The low card is " + hand.lowCard());
		System.out.println();
		
		hand.replaceCard(2, twoDiamonds);
		System.out.println(hand);
		System.out.println("The low card is " + hand.lowCard());
		
	}
}