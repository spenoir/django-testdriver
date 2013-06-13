jasmine.getFixtures().fixturesPath = FIXTURES_PATH;


describe('sidebar loaded', function() {

	beforeEach(function() {
		loadFixtures('sidebar.html');
	});

	it('should load sidebar', function() {

		expect($('#sidebar div:first')).toHaveClass('toolbar-actions-container');
	});
});