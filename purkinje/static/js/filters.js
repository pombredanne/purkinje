;
(function() {
    'use strict';

    /**
     * Gives CSS class for test verdict
     */
    angular
        .module('purkinje')
        .filter('verdictClassFilter', function() {
            return verdictClassFilter;
        });

    function verdictClassFilter(verdict, cssClass) {
        switch (verdict) {
            case defs.Verdict.PASS:
                return 'success';
            case defs.Verdict.FAIL:
                return 'danger';
            case defs.Verdict.ERROR:
                return 'warning';
            default:
                return 'default';
        };
    };
})();