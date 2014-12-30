window.util = {
    /**
     * Computes counts of verdicts to display summary
     */
    countVerdicts: function(testResults) {
        result =  _.countBy(testResults, function(item) {
            return item.verdict;
        });
        result.all = testResults.length;
        return result;
    }
};
