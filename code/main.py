import preprocessing_realtime as pr
import classify_realtime as cr

def run():
    # pr.preprocessing()
    
    classification, overall_emotion_value, time = cr.classify_fisherface()
    print "Capture time: %s" %time
    print classification
    print "Overall Emotion Value: %s" %overall_emotion_value

    return classification, overall_emotion_value, time
