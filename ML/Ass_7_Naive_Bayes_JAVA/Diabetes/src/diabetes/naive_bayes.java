package diabetes;

import java.io.BufferedReader;
import java.io.FileReader;

import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayes;
import weka.core.Instances;

public class naive_bayes
{
	naive_bayes()
	{
		try
		{
			BufferedReader training  = new BufferedReader(new FileReader("/home/test/BE/CL-7_practice/ML/Ass_7_Naive_Bayes_JAVA/WEKAdiabetesTr.arff"));
			BufferedReader testing  = new BufferedReader(new FileReader("/home/test/BE/CL-7_practice/ML/Ass_7_Naive_Bayes_JAVA/WEKAdiabetesTest.arff"));

			
			Instances train = new Instances(training);
			Instances test = new Instances(testing);
			
			train.setClassIndex(train.numAttributes() - 1);
			test.setClassIndex(test.numAttributes() - 1);
			
			
			NaiveBayes model = new NaiveBayes();
			model.buildClassifier(train);
			
			Evaluation result = new Evaluation(test);
			result.evaluateModel(model, test);
			
			
			System.out.printf("Accuracy = %.3f\n", result.pctCorrect());
			System.out.printf("Error = %.3f\n", result.errorRate()*100);
			
			for(int i=0; i<train.numClasses(); i++)
			{
				System.out.println("-------CLASS " + (i+1) + "--------------");
				
				System.out.printf("Precision = %.3f\n", result.precision(i));
				System.out.printf("Recall = %.3f\n", result.recall(i));
				System.out.printf("FPR = %.3f\n", result.falsePositiveRate(i));
				System.out.printf("FNR = %.3f\n", result.falseNegativeRate(i));
				System.out.printf("TNR = %.3f\n", result.trueNegativeRate(i));
				
			}
			
			
		}
		
		catch (Exception e) 
		{
			System.err.println("Error in Naive Bayes : "+ e.getMessage());
		}
	}
	
	public static void main(String Args[])
	{
		naive_bayes Naive_Bayes = new naive_bayes();
	}
}
