# Load the packages for analysis
library(ggplot2)
library(lme4)
library(lmerTest)

##Reading in the data file
#f <- read.csv("C:/Users/scarl/Desktop/LSA/dataset_for_GCA.csv", encoding = 'UTF-8')
# I prefer to import the dataset manually on RStudio
f <- dataset_for_GCA 

# 1. Preparing data: Subset two values of one variable
T25 <- subset(f, subset = citation_tone %in% c("2","5"))
T25_80s <- subset(T25, subset = year %in% c("1980s"))
T25_90s <- subset(T25, subset = year %in% c("1990s"))
T25_2000 <- subset(T25, subset = year %in% c("after2000"))

# T36 <- subset(f, subset = citation_tone %in% c("3","6"))
# T36_80s <- subset(T36, subset = year %in% c("1980s"))
# T36_90s <- subset(T36, subset = year %in% c("1990s"))
# T36_2000 <- subset(T36, subset = year %in% c("after2000"))
# 
# T46 <- subset(f, subset = citation_tone %in% c("4","6"))
# T46_80s <- subset(T46, subset = year %in% c("1980s"))
# T46_90s <- subset(T46, subset = year %in% c("1990s"))
# T46_2000 <- subset(T46, subset = year %in% c("after2000"))

table(is.na(T25_80s$word_type))

# ggplot(T25_90s, aes(Position, f0, shape=citation_tone)) +
#   stat_summary(fun.data = mean_se, geom="pointrange")


# 3. non-linear modeling (Chapman & Hall, 2014, p. 51-)
# Which order? Quadratic, cubic or quartic? Generally it could be based on how many times the curve changes direction (formally, the number of inflection points) (p. 46)

t <- poly(unique(T25_80s$Position),2)
T25_80s[,paste("ot",1:2,sep = "")] <- t[T25_80s$Position, 1:2]

t25.base <- lmer(f0 ~ (ot1+ot2) + (ot1+ot2 | word_type),
               data = T25_80s, REML = FALSE)
t25.0 <- lmer(f0 ~ (ot1 + ot2) + citation_tone + (ot1+ot2 | word_type),
             data = T25_80s, REML = FALSE)
t25.1 <- lmer(f0 ~ (ot1 + ot2) + citation_tone + ot1:citation_tone +
               (ot1 + ot2 | word_type),
             data = T25_80s, REML = FALSE)
t25.2 <- lmer(f0 ~ (ot1+ot2)*citation_tone + (ot1+ot2 | word_type),
             data = T25_80s, REML = FALSE)

t25_coefs <- data.frame(coef(summary(t25.2)))
t25_coefs$p <- 2 * (1 - pnorm(abs(t25_coefs$t.value)))
t25_coefs$year <- '1980s'

anova(t25.base, t25.0,t25.1,t25.2)

ggplot(T25_80s, aes(Position, f0, shape=citation_tone)) +
  stat_summary(aes(y=fitted(t25.2), linetype=citation_tone),fun.y = mean,
               geom = "line", size=1)+
  stat_summary(fun.data = mean_se,geom="pointrange",size=0.8)+
  theme_bw(base_size = 10)+
  coord_cartesian(ylim=c(85.0, 95.0))+
  scale_x_continuous(breaks=1:8)

t25_coef_all <- rbind(t25_coefs, t25_90_coefs, t25_20_coefs)s

write.csv(t25_coef_all,file = 'C:/Users/scarl/Desktop/LSA/gca_coefs_T25.csv')

# # report GCA results (p/ 58)
# 1. the model structure: the functional form, all of the fixed and random effects
# 2. the basis for the inferential statistics
# - for model conparisons
# - for parameter-specific p-values, normal approximation was used
# 3. complete modek results, not just p-values
# - for model comparisons, change in log-likelihood & degrees of freedom
# - for parameter estimates, the estimates and their standard errors
