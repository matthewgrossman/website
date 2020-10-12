module.exports = function(eleventyConfig) {
    eleventyConfig.addPassthroughCopy("static");
    eleventyConfig.addPassthroughCopy("CNAME");
    // return {
    //     dir: {
    //         output: "docs"
    //     },
    //     pathPrefix: '/website/'
    // }
};
