FROM opensearchproject/opensearch:2.19.0

# Download OpenTelemetry Java agent
USER root
RUN curl -L -o /usr/share/opensearch/lib/opentelemetry-javaagent.jar \
    https://github.com/open-telemetry/opentelemetry-java-instrumentation/releases/latest/download/opentelemetry-javaagent.jar

# Copy custom security policy for OpenTelemetry
COPY otel.policy /usr/share/opensearch/config/otel.policy

# Create a custom security policy that includes both OpenSearch and OTEL permissions
RUN cat /usr/share/opensearch/config/opensearch-performance-analyzer/opensearch_security.policy > /usr/share/opensearch/config/combined_security.policy && \
    echo "" >> /usr/share/opensearch/config/combined_security.policy && \
    cat /usr/share/opensearch/config/otel.policy >> /usr/share/opensearch/config/combined_security.policy

# Set proper ownership
RUN chown -R opensearch:opensearch /usr/share/opensearch/config/ && \
    chown opensearch:opensearch /usr/share/opensearch/lib/opentelemetry-javaagent.jar

# Switch back to opensearch user
USER opensearch
