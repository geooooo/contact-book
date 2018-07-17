var gulp = require('gulp');
var scss = require('gulp-sass');
var pug  = require('gulp-pug');


var PATHS = {
    scss: [
        // 'components/*/*.scss',
        'index.scss',
    ],
    pug: [
        // 'components/*/*.pug',
        'index.pug',
    ],
};


gulp.task('compile-scss', function () {
    return gulp.src(PATHS.scss)
               .pipe(scss({
                    outputStyle: 'expanded',
               }))
               .pipe(gulp.dest('.'));
});


gulp.task('compile-pug', function () {
    return gulp.src(PATHS.pug)
               .pipe(pug({
                    pretty: true,
               }))
               .pipe(gulp.dest('.'));
});


gulp.task('compile', function () {
    gulp.watch(PATHS.scss, gulp.series('compile-scss'));
    gulp.watch(PATHS.pug,  gulp.series('compile-pug'));
});
