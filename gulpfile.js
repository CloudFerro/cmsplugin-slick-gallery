var gulp = require('gulp');

// remove files and folders
// var clean = require('gulp-clean');

var sass = require('gulp-sass');

//exec shell script
var exec = require('child_process').exec;

// concat files into one
var concat = require('gulp-concat');

var cleanCSS = require('gulp-clean-css');
var sourcemaps = require('gulp-sourcemaps');

var terser = require('gulp-terser');

// var minifyHTML = require('gulp-minify-html');

var autoprefixer = require('gulp-autoprefixer');
require('es6-promise').polyfill();

var merge = require('merge-stream');

var sassdoc = require('sassdoc');

//gulp-ng-annotate Makes angular safe to minify.
//var merge = require('merge-stream');

var inputPaths = {
	sass: [
		'./static_dev/scss/**/*.scss'
	],
	css: [
		'./static_dev/css/**/*.css'
	],
	js: [
	]
};

var outputPaths = {
	css: './src/cmsplugin_filer_gallery/templates/media/css/',
	js: './src/cmsplugin_filer_gallery/templates/media/js/',
	sassdoc: './src/cmsplugin_filer_gallery/templates/media_dev/sassdoc/'
};

var autoprefixerOptions = {
	browsers: ['last 2 versions', '> 5%', 'Firefox ESR']
};

var sassOptions = {
	outputStyle: 'compressed',
	errLogToConsole: true
};

var sassdocOptions = {
	dest: outputPaths.sassdoc
};


gulp.task('sassdoc', function () {
	return gulp.src(inputPaths.sass)
		.pipe(sassdoc(sassdocOptions))
		.resume();
});

gulp.task('compile_merge_styles', function () {
	var sassStream,
		cssStream;
	sassStream = gulp
		.src(inputPaths.sass)
		.pipe(sass(sassOptions).on('error', sass.logError))
	cssStream = gulp.src(inputPaths.css)
	return merge(sassStream, cssStream)
		.pipe(concat('styles.min.css'))
		.pipe(sourcemaps.init())
		.pipe(autoprefixer())
		.pipe(cleanCSS({ compatibility: '*', keepSpecialComments: '0' }))
		.pipe(sourcemaps.write())
		.pipe(gulp.dest(outputPaths.css));
});


gulp.task('compress_js', function () {
	return gulp.src(inputPaths.js)
		.pipe(concat('all.min.js')) // set concated file name
		//    .pipe(annotate()) // Makes angular safe to minify.
		.pipe(terser()) // Minifies the concatenated js file.
		.pipe(gulp.dest(outputPaths.js)); // sets destination folder
});


gulp.task('default', gulp.series(gulp.parallel('compile_merge_styles', 'compress_js'), 'sassdoc'), function () {
	console.log('Witaj.');
});

gulp.task('watch', function () {
	return gulp
		// Watch the input folder for change,
		// and run `sass` task when something happens
		.watch(inputPaths.sass.concat(inputPaths.js),
			gulp.parallel('compile_merge_styles')) //,'compress_js' 
		// When there is a change,
		// log a message in the console
		.on('change', function (event) {
			console.log('File ' + event + ', running tasks...');
		});
});
